function lpdcPostCal()
    %% Get ini and log filenames
    % Location to look for ini and log file
    file_path = '\luminartech\P99.9_LPDC\LPDC_Paramters\LPDC_Landing_Zone';
    
    % Get the ini file
    ini_dir = dir(fullfile(file_path, '*.ini'));
    ini_filename = fullfile(ini_dir(1).folder, ini_dir(1).name);
    
    % Get the log file
    log_dir = dir(fullfile(file_path, '*.txt'));
    log_filename = fullfile(log_dir(1).folder, log_dir(1).name);

    %% Open ini file
    ini_fp = fopen(ini_filename, 'r');
    if ini_fp == -1
        error('Could not open ini file.');
    end

    %% Extract range offsets
    % Go through each line looking for the RngCoefficients
    rng_offset_line = fgets(ini_fp);
    found = false;
    while rng_offset_line ~= -1
        k = strfind(rng_offset_line, 'RngCoefficients=');

        % If not found, go to the next line. If found, stop the loop
        if isempty(k)
            rng_offset_line = fgets(ini_fp);
        else
            found = true;
            break;
        end
    end

    % Verify that we found the line containing RngCoefficients
    if found == false
        error('Could not find RngCoefficients in ini file.');
    end

    % Parse the line to extract the range offsets
    temp_line = strrep(rng_offset_line, 'RngCoefficients=', '');
    temp_line = strrep(temp_line, ',', '');
    rng_offsets = sscanf(temp_line, '%f');

    %% Close ini file
    fclose(ini_fp);

    %% Open log file
    log_fp = fopen(log_filename, 'r');
    if log_fp == -1
        error('Could not open log file.');
    end

    %% Extract lpdc values
    % Go through all the lines in the file
    lpdc_line = fgets(log_fp);
    idx = 1;
    while lpdc_line ~= -1
        % Check for an LPDC line
        k = strfind(lpdc_line, 'LPDC Det0');

        if ~isempty(k)
            % Attempt to extract the values. If it fails, then read in the
            % next line and concatenate until it succeeds.
            lpdc_values = sscanf(lpdc_line, '[%f] LPDC Det0 Energy=%f Range=%f T0=%f Det1 Energy=%f Range=%f T0=%f\n');
            while length(lpdc_values) < 7
                lpdc_line_next = fgets(log_fp);
                lpdc_line = [lpdc_line lpdc_line_next];
                lpdc_values = sscanf(lpdc_line, '[%f] LPDC Det0 Energy=%f Range=%f T0=%f Det1 Energy=%f Range=%f T0=%f\n');
            end

            % Extract the values
            det0_range(idx) = lpdc_values(3);
            det0_t0(idx) = lpdc_values(4);
            det1_range(idx) = lpdc_values(6);
            det1_t0(idx) = lpdc_values(7);
            idx = idx + 1;
        end

        % Read the next line
        lpdc_line = fgets(log_fp);
    end

    %% Close log file
    fclose(log_fp);

    %% Apply conversion
    % Select the median value from all the inputs
    det0_range_median = median(det0_range);
    det0_t0_median = median(det0_t0);
    det1_range_median = median(det1_range);
    det1_t0_median = median(det1_t0);

    tdc2meters = 7.716E-11 / 1.000268502 * 299792458 / 2;
    site_a_fixed_delay_offset = 0;
    site_b_fixed_delay_offset = 0;
    det0_et0_rng = ((det0_range_median - det0_t0_median) * tdc2meters / 4) - (site_a_fixed_delay_offset * tdc2meters);
    det1_et0_rng = ((det1_range_median - det1_t0_median) * tdc2meters / 4) - (site_b_fixed_delay_offset * tdc2meters);

    rng_offset_det0 = rng_offsets(8);
    rng_offset_det1 = rng_offsets(40);

    adjusted_rng_offset_det0 = rng_offset_det0 - det0_et0_rng;
    adjusted_rng_offset_det1 = rng_offset_det1 - det1_et0_rng;

    %% Update range offsets line
    det0_str = sprintf('0, 0, 0, 0, 0, 0, 0, %0.10f', adjusted_rng_offset_det0);
    det1_str = sprintf('0, 0, 0, 0, 0, 0, 0, %0.10f', adjusted_rng_offset_det1);
    new_rng_offset_line = ['RngCoefficients=' det0_str ', ' det0_str ', ' det0_str ', ' det0_str ', ' det1_str ', ' det1_str ', ' det1_str ', ' det1_str];

    %% Write new range offsets back to ini file
    % Get the new filename to create
    [~, name, ext] = fileparts(ini_dir(1).name);
    ini_file_new = [name '_lpdc' ext];
    ini_filename_new = fullfile(ini_dir(1).folder, ini_file_new);

    % Create the new file for writing
    ini_fp_new = fopen(ini_filename_new, 'w');
    if ini_fp_new == -1
        error('Could not create updated INI file');
    end

    % Open the old file
    ini_fp = fopen(ini_filename, 'r');
    if ini_fp == -1
        error('Could not open ini file');
    end

    % Go through each line and write it out to the new ini file. Except for the
    % RngCoefficients and HasLpdcTarget lines which are substituted for the new
    % lines
    rng_offset_updated = false;
    has_lpdc_target_updated = false;
    line = fgets(ini_fp);
    while line ~= -1
        % Look for the specified lines
        k = strfind(line, 'RngCoefficients=');
        l = strfind(line, 'HasLpdcTarget=');

        if ~isempty(k)
            % This is the RngCoefficients line, so write out the new line to
            % the output ini file
            fprintf(ini_fp_new, '%s\n', new_rng_offset_line);
            rng_offset_updated = true;
        elseif ~isempty(l)
            % This is the HasLpdcTarget line, so write out the new line to the
            % output ini file
            fprintf(ini_fp_new, 'HasLpdcTarget=1\n');
            fprintf(ini_fp_new, 'LpdcDelayCompensation=%d,%d\n', site_a_fixed_delay_offset, site_b_fixed_delay_offset);
            has_lpdc_target_updated = true;
        else
            % This is not the line we're looking for, so just copy the current
            % line to the output ini file
            fprintf(ini_fp_new, '%s', line);
        end

        line = fgets(ini_fp);
    end

    % Close the files
    fclose(ini_fp);
    fclose(ini_fp_new);

    %% Verify that the updates to the ini file have been made
    % RngOffset
    if rng_offset_updated == false
        error('Could not update RngCoefficients');
    end

    % HasLpdcTarget
    if has_lpdc_target_updated == false
        error('Could not update HasLpdcTarget');
    end

    %% Copy the resulting ini file to a user selected location
    % Prompt user for copy location
    %[copy_file, copy_path] = uiputfile('*.ini', 'Copy INI File to New Location', ini_filename_new);

    % Check for user cancellation
    %if copy_file == 0
       % error('User cancelled ini file copy');
    %end

    % Copy the file to the new location
    %ini_filename_copy = fullfile(copy_path, copy_file);
    %status = copyfile(ini_filename_new, ini_filename_copy, 'f');

    % Verify copy was successful
    %if status == 0
      %  error('Could not copy ini file to new location');
    %end
end

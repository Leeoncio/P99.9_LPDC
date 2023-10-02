<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="18008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="collect_data.vi" Type="VI" URL="../collect_data.vi"/>
		<Item Name="config_optom.vi" Type="VI" URL="../config_optom.vi"/>
		<Item Name="draw_plot.vi" Type="VI" URL="../draw_plot.vi"/>
		<Item Name="initialize.vi" Type="VI" URL="../initialize.vi"/>
		<Item Name="laser-level(1).ico" Type="Document" URL="../../../Users/P3-Martin.bustamante/Downloads/laser-level(1).ico"/>
		<Item Name="Main.vi" Type="VI" URL="../Main.vi"/>
		<Item Name="Main_v2.vi" Type="VI" URL="../Main_v2.vi"/>
		<Item Name="measure.vi" Type="VI" URL="../measure.vi"/>
		<Item Name="pulse energy.vi" Type="VI" URL="../pulse energy.vi"/>
		<Item Name="release_handle.vi" Type="VI" URL="../release_handle.vi"/>
		<Item Name="Save_energy.vi" Type="VI" URL="../Save_energy.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="user.lib" Type="Folder">
				<Item Name="GOMDTR9600.dll" Type="Document" URL="/&lt;userlib&gt;/Gigahertz-Optik/runtimeX64/GOMDTR9600.dll"/>
				<Item Name="GOMDTR9600.lvlib" Type="Library" URL="/&lt;userlib&gt;/Gigahertz-Optik/GOMDTR9600/GOMDTR9600.lvlib"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Write Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Write Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (I64).vi"/>
				<Item Name="Write Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (string).vi"/>
				<Item Name="Write Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet.vi"/>
				<Item Name="Write Spreadsheet String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Spreadsheet String.vi"/>
			</Item>
			<Item Name="GOMDTR9600 get Page.vi" Type="VI" URL="../../../Program Files/National Instruments/LabVIEW 2018/user.lib/Gigahertz-Optik/GOMDTR9600/GOMDTR9600 get Page.vi"/>
			<Item Name="GOMDTR9600 get Sampling Rate.vi" Type="VI" URL="../../../Program Files/National Instruments/LabVIEW 2018/user.lib/Gigahertz-Optik/GOMDTR9600/GOMDTR9600 get Sampling Rate.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="MPE_Analyzer" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{308A256C-A790-46A5-A6FE-9B7467D957C6}</Property>
				<Property Name="App_INI_GUID" Type="Str">{1B22E759-497A-4ECA-BF79-8E4B3E98B1FB}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{99BEA6F4-47B3-4622-BB12-4FF6713A2152}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">MPE_Analyzer</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/MPE_Analyzer</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{233011FD-1D15-40AA-AD51-8E018609E930}</Property>
				<Property Name="Bld_version.build" Type="Int">1</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">MPE_Analyzer.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/MPE_Analyzer/MPE_Analyzer.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/MPE_Analyzer/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Exe_iconItemID" Type="Ref">/My Computer/laser-level(1).ico</Property>
				<Property Name="Source[0].itemID" Type="Str">{4CD2D6AF-A6A5-4BBD-9863-BF8E7714F135}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Main_v2.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">Luminar Technologies</Property>
				<Property Name="TgtF_fileDescription" Type="Str">MPE_Analyzer</Property>
				<Property Name="TgtF_internalName" Type="Str">MPE_Analyzer</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2022 Luminar Technologies</Property>
				<Property Name="TgtF_productName" Type="Str">MPE_Analyzer</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{6CF573CD-085D-44A0-9880-E4600A8902DD}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">MPE_Analyzer.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>

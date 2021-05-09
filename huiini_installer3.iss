; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Huiini"
#define MyAppVersion "1.6.2"
#define MyAppPublisher "Huiini"
#define MyAppURL "http://huiini.com.mx"
#define MyAppExeName "huiini.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{6CC2D6FC-08F1-4E34-A7F4-ADA14F78B7AA}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=LICENSE
OutputBaseFilename=huiiniInstaller
SetupIconFile=myicon.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\huiini\huiini.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\huiini\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "*.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "*.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "*.jinja"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\huiini_aux_files\pdflatex_path.txt"; DestDir: "{userdocs}\huiini"; Flags: ignoreversion onlyifdoesntexist uninsneveruninstall
Source: "..\huiini_aux_files\template_diot.xlsx"; DestDir: "{userdocs}\huiini"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

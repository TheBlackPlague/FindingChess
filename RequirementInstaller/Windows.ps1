# Ensure Chocolatey is installed
if (-not (Test-Path -Path "$env:ProgramData\chocolatey\choco.exe")) {
    Write-Output "Installing Chocolatey..."
    Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}

# List of packages to install
$packages = @('llvm', 'go', 'cmake', 'make', 'python', 'git', 'ninja', 'visualstudio2022buildtools')

# Loop through each package and install it
foreach ($package in $packages) {
    Write-Output "Installing $package..."
    if ($package -eq 'visualstudio2022buildtools') {
        choco install $package --package-parameters "--add Microsoft.VisualStudio.Workload.VCTools --includeRecommended" -y
    } else {
        choco install $package -y
    }
}

Write-Output "All packages installed successfully."

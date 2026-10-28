# PowerShell 1-Click Test Runner
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host "  CHẠY KIỂM THỬ TỰ ĐỘNG SELENIUM WEBDRIVER (SWAG LABS - SAUCEDEMO)" -ForegroundColor Cyan
Write-Host "  Sinh viên: Phạm Duy Quang - MSSV: 23017167 - Lớp: AI&KHDL_1" -ForegroundColor Cyan
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host ""

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

$VenvPython = Join-Path $ScriptDir ".venv\Scripts\python.exe"

if (Test-Path $VenvPython) {
    Write-Host "[INFO] Đang chạy với môi trường ảo .venv..." -ForegroundColor Green
    & $VenvPython run_tests.py
} else {
    Write-Host "[INFO] Đang chạy với Python hệ thống..." -ForegroundColor Yellow
    python run_tests.py
}

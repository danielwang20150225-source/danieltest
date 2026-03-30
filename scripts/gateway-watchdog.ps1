# Gateway Watchdog - 在 exec 外部重启网关，保证重连能力
# 使用 schtasks 操作 \OpenClaw Gateway 定时任务，不依赖 Gateway 进程
param(
    [int]$WaitSeconds = 15,
    [int]$MaxRetries = 20,
    [string]$TaskName = "\OpenClaw Gateway"
)

$ErrorActionPreference = "Continue"

function Get-GatewayHealth {
    try {
        $null = Invoke-WebRequest -Uri "http://127.0.0.1:18789/" -TimeoutSec 3 -UseBasicParsing -ErrorAction SilentlyContinue
        return $true
    } catch {
        return $false
    }
}

# Main logic
Write-Host "[Watchdog] Triggering gateway restart via schtasks..."

# End current gateway task
schtasks /End /TN $TaskName 2>&1 | Out-Null
Start-Sleep 2

# Start gateway task again
schtasks /Run /TN $TaskName 2>&1 | Out-Null
Write-Host "[Watchdog] Gateway restart triggered"

# Wait for gateway to come back up
Write-Host "[Watchdog] Waiting ${WaitSeconds}s for gateway to initialize..."
Start-Sleep $WaitSeconds

for ($i = 1; $i -le $MaxRetries; $i++) {
    if (Get-GatewayHealth) {
        Write-Host "[Watchdog] Gateway is back up after $i checks"
        exit 0
    }
    Write-Host "[Watchdog] Gateway not ready, waiting... ($i/$MaxRetries)"
    Start-Sleep 5
}

Write-Host "[Watchdog] WARNING: Gateway did not come back within expected time"
exit 1

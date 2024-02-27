Add-Type -AssemblyName System.Windows.Forms
$screenCount = [System.Windows.Forms.Screen]::AllScreens.Count
Write-Host "Número de telas conectadas: $screenCount"

for ($i = 0; $i -lt $screenCount; $i++) {
    $screen = [System.Windows.Forms.Screen]::AllScreens[$i]
    Write-Host "Tela $i - Resolução: $($screen.Bounds.Width)x$($screen.Bounds.Height), Coordenadas: $($screen.Bounds.X), $($screen.Bounds.Y)"
}

$exclude = @("venv", "BotCampoMinado.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BotCampoMinado.zip" -Force
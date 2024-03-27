$exclude = @("venv", "Desafio_RPA_–_Com_BotCity.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Desafio_RPA_–_Com_BotCity.zip" -Force
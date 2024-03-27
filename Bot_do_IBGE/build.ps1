$exclude = @("venv", "Bot_do_IBGE.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Bot_do_IBGE.zip" -Force
$exclude = @("venv", "BotYoutube_treino_2.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BotYoutube_treino_2.zip" -Force
$folders = @(
    "handbook",
    "notebooks",
    "labs",
    "code",
    "docs",
    "glossary",
    "quizzes",
    "troubleshooting",
    "capstone",
    "images"
)

foreach ($folder in $folders) {
    New-Item -ItemType File -Path "$folder\.gitkeep" -Force
}
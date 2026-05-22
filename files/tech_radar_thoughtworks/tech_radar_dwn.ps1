$BaseUrl = "https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar"

$Radars = @{
    34 = "2026/04"
    33 = "2025/10"
    32 = "2025/04"
    31 = "2024/10"
    30 = "2024/04"
    29 = "2023/09"
    28 = "2023/04"
    27 = "2022/10"
    26 = "2022/03"
    25 = "2021/10"
    24 = "2021/04"
    23 = "2020/10"
    22 = "2020/05"
    21 = "2019/11"
    20 = "2019/04"
    19 = "2018/11"
    18 = "2018/05"
    17 = "2017/11"
    16 = "2017/03"
    15 = "2016/11"
    14 = "2016/04"
    13 = "2015/11"
    12 = "2015/05"
    11 = "2015/01"
    10 = "2014/07"
    9  = "2014/01"
    8  = "2013/05"
    7  = "2012/10"
    6  = "2012/03"
    5  = "2011/07"
    4  = "2011/01"
    3  = "2010/08"
    2  = "2010/04"
    1  = "2010/01"
}

$OutputDir = "."

# Optional: ensure current directory exists/resolves
$OutputDir = (Resolve-Path $OutputDir).Path

foreach ($Vol in ($Radars.Keys | Sort-Object -Descending)) {

    $DatePath = $Radars[$Vol]
    $FileName = "tr_technology_radar_vol_${Vol}_en.pdf"
    $Url = "$BaseUrl/$DatePath/$FileName"

    $OutputFile = Join-Path $OutputDir ("vol_{0:D2}.pdf" -f $Vol)

    if (Test-Path $OutputFile) {
        Write-Host "Skipping Vol $Vol (already exists)"
        continue
    }

    Write-Host "Downloading Vol $Vol ..."
    
    Invoke-WebRequest `
        -Uri $Url `
        -OutFile $OutputFile

    Write-Host "Saved -> $OutputFile"
}

Write-Host "Done."
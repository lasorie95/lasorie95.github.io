param(
    [ValidateSet('Install', 'Preview')]
    [string]$Mode = 'Preview'
)

$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)

$rubyBin = Join-Path $env:USERPROFILE 'Ruby33-x64\bin'
if (Test-Path -LiteralPath $rubyBin -PathType Container) {
    $env:PATH = "$rubyBin;$env:PATH"
}
$env:RUBYOPT = "$env:RUBYOPT -EUTF-8".Trim()
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding($false)
$OutputEncoding = [Console]::OutputEncoding

# Keep proxy settings only in this process and its child processes.
try {
    $systemProxy = [System.Net.WebRequest]::GetSystemWebProxy()
    foreach ($scheme in @('http', 'https')) {
        $variableName = "${scheme}_proxy"
        if (-not [Environment]::GetEnvironmentVariable($variableName, 'Process')) {
            $destination = [uri]"${scheme}://rubygems.org"
            if (-not $systemProxy.IsBypassed($destination)) {
                $proxyUri = $systemProxy.GetProxy($destination)
                if ($proxyUri -and $proxyUri -ne $destination) {
                    [Environment]::SetEnvironmentVariable($variableName, $proxyUri.AbsoluteUri, 'Process')
                }
            }
        }
    }
} catch {
    throw 'Could not read Windows system proxy settings.'
}

$bypassHosts = @($env:no_proxy -split ',' | ForEach-Object { $_.Trim() } | Where-Object { $_ })
$bypassHosts += @('localhost', '127.0.0.1', '::1')
$env:no_proxy = ($bypassHosts | Select-Object -Unique) -join ','

if ($Mode -eq 'Install') {
    & bundle config set --local path vendor/bundle
    if ($LASTEXITCODE -ne 0) {
        exit $LASTEXITCODE
    }
    & bundle install
} else {
    & bundle exec jekyll serve --livereload --force_polling --drafts --host 127.0.0.1 --open-url
}
exit $LASTEXITCODE

param(
    [Parameter(Position = 0)][string]$Command,
    [Parameter(Position = 1, ValueFromRemainingArguments = $true)]$Rest
)

switch ($Command) {
    "build" {
        & $PSCommandPath lint:fix
        & $PSCommandPath format
        & $PSCommandPath test
    }
    "format" {
        & uv run black $PSScriptRoot
    }
    "test" {
        & uv run pytest $PSScriptRoot -q
    }
    "lint" {
        & uv run ruff check .
    }
    "lint:fix" {
        & uv run ruff check . --fix
    }
    "run" {
        & uv run $PSScriptRoot/main.py $Rest
    }
    "install" {
        & uv add $Rest
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
        & uv lock
    }
    "uninstall" {
        & uv remove $Rest
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
        & uv lock
    }
    "help" {
        Write-Host "Usage: local.ps1 <command> [args]"
        Write-Host ""
        Write-Host "Commands:"
        Write-Host "  build         Run lint, format, and test"
        Write-Host "  format        Format the code using black"
        Write-Host "  test          Run tests using pytest"
        Write-Host "  lint          Run lint using ruff"
        Write-Host "  lint:fix      Run lint using ruff and fix issues"
        Write-Host "  run           Run the script"
        Write-Host "  install       Install a package and update requirements.txt"
        Write-Host "  uninstall     Uninstall a package and update requirements.txt"
        Write-Host "  help          Show this help message"
    }
    default {
        Write-Error "Command '$Command' not found."
        Write-Host

        & $PSCommandPath help
    }
}

exit $LASTEXITCODE

trap {
    Write-Error $_
    exit 1
}
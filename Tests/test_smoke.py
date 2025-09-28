def test_cli_runs():
    from subprocess import run, PIPE
    import sys
    r = run([sys.executable, "-m", "dflab"], stdout=PIPE, text=True)
    assert r.returncode == 0
    assert "dflab" in r.stdout.lower()

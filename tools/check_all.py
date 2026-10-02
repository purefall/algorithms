from pathlib import Path
import subprocess
import sys
root=Path(__file__).resolve().parents[1]
failed=[]
for test in sorted((root/'problems').glob('*/*/tests.py')):
    args=[sys.executable,str(test)]
    if '--solution' in sys.argv: args.append('--solution')
    result=subprocess.run(args,capture_output=True,text=True)
    print(('PASS' if result.returncode==0 else 'FAIL'),test.parent.name)
    if result.returncode:
        failed.append(test.parent.name)
        print(result.stdout+result.stderr)
print(f'{30-len(failed)}/30 problem suites passed')
sys.exit(bool(failed))

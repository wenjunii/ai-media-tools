"""Read-only Git index guard for PC source handoff; never pushes or publishes."""
import pathlib
import subprocess
from .common import ROOT

SOURCE_SUFFIXES={'.py','.ps1','.md','.json','.txt','.html','.css','.js'}


def validate_index_entry(name, size):
    path=pathlib.PurePosixPath(name)
    if not name.startswith('pc_demo/'):
        return
    if any(part in {'.local','.venv','__pycache__','node_modules'} for part in path.parts):
        raise ValueError(f'Private PC runtime path in Git index: {name}')
    if path.suffix.lower() not in SOURCE_SUFFIXES or name.endswith('.local.json'):
        raise ValueError(f'Only reviewed PC source and documentation belong in Git: {name}')
    if size>1024*1024:
        raise ValueError(f'Unexpected large PC file in Git index: {name}')


def audit_git():
    result=subprocess.run(['git','ls-files','-z','--','pc_demo'],cwd=ROOT.parent,
                          check=True,capture_output=True)
    names=[x for x in result.stdout.decode('utf-8').split('\0') if x]
    for name in names:
        content=subprocess.run(['git','show',':'+name],cwd=ROOT.parent,check=True,capture_output=True).stdout
        validate_index_entry(name,len(content))
    return {'passed':True,'pc_source_files_checked':len(names),'mode':'read-only staged index; no publication'}

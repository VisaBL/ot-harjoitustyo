from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/main.py")

@task 
def test(ctx):
    ctx.run("pytest")
   
@task
def run_event_tests(ctx):
    ctx.run("pytest src/tests/eventq_test.py")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
    
@task(coverage)
def coverage_terminal(ctx):
    ctx.run("coverage report -m")

@task 
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")
   
@task
def lint(ctx):
    ctx.run("pylint src") 

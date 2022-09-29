import nox

nox.options.sessions = ["bench"]

@nox.session
def bench(session):
    session.install("-rrequirements-dev.txt")
    session.run("pytest", "--benchmark-enable")

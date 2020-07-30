# cmd structure -- script,amount,stage:
def executeCommand(Command):
    if "farm" in Command:
        pass
    if "train" in Command:
        script, amount, stage = Command.split(",")
        print("Script: " + script)
        print("Amount: " + amount)
        print("Stage: " + stage)
        return "done."
    if "tut" in Command:
        pass
    if "create" in Command:
        pass
    if "" in Command:
        pass

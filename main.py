def check_log(user_prompt: str) -> dict[str, str]:
    print(f"call check_log")
    print(f"user_prompt: {user_prompt}")
    status = "OK"
    resp = "check log ok"
    return {"resp": resp, "status": status}


def run_iteration(user_prompt: str) -> dict[str, str]:
    print(f"call run_iteration")
    print(f"user_prompt: {user_prompt}")
    status = "OK"
    resp = "run iteration OK"
    return {"resp": resp, "status": status}


def xrun(user_prompt: str) -> dict[str, str]:
    print(f"call xrun")
    print(f"user_prompt: {user_prompt}")
    status = "OK"
    resp = "xrun OK"
    return {"resp": resp, "status": status}


registered_tools = {
    "run_iteration": {"id": 1111, "func": run_iteration},
    "check_log": {"id": 2222, "func": check_log},
    "run_simulator": {"id": 3333, "func": xrun},
}


def get_tool_name_str(name: str, tools: dict = {}) -> str:
    tool = "None"
    if tools[name] is not None:
        tool = tools[name]
    else:
        print("error")

    return tool


def tool_call(name: str, tools: dict = {}) -> dict[str, str]:
    tool = "None"
    resp = "None"
    status = "NG"

    for tool_name, val in tools.items():
        if name == tool_name:
            function = val["func"]
            if function is not None:
                r = function(user_prompt)
                print(f"resp of {tool_name} = {r['resp']}, status = {r['status']} ")
                tool = tool_name
                resp = r["resp"]
                status = r["status"]

    if tool == "None":
        print(f"ERROR: tool name is None")

    return {
        "tool": tool,
        "resp": resp,
        "status": status,
    }


def main():
    print(f"this is main!")


if __name__ == "__main__":
    main()
    user_prompt = "get the current prompt"

    res_run_sim = tool_call("run_simulator", registered_tools)
    print(f"stats = {res_run_sim['status']}, tool = {res_run_sim['tool']}")

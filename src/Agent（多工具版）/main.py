from agent import run_agent

def main():
    while True:
        q = input("请输入问题（exit退出）：")
        if q == "exit":
            break

        run_agent(q)

if __name__ == "__main__":
    main()
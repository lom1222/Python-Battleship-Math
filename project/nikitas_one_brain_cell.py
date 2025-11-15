import time

from project.neat_agent import *



def main():
    start_time = time.time()
    agent = Agent(meta_generation="test", agent_id="setup_time_", inputs=100, outputs=100, hidden=1)
    agent.basic_setup()
    print("Total Time: " + str(round(time.time() - start_time, 5)) + "s")
    file_path = agent.save()
    print("Total Time: "+str(round(time.time()-start_time,5))+"s")
    agent.load_from_file(file_path)
    return print("Total Time: " + str(round(time.time() - start_time, 5)) + "s")

main()
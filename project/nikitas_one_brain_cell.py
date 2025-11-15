import time

from project.neat_agent import *



def main():
    start_time = time.time()
    agent = Agent(meta_generation="test", agent_id="large", inputs=1000, outputs=1000, hidden=100)
    agent.basic_setup()
    print("Total Time: " + str(round(time.time() - start_time, 6)) + "s")
    agent.save()
    print("Total Time: "+str(round(time.time()-start_time,6))+"s")

main()
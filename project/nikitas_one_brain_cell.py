import time

from project.neat_agent import *



def main():
    start_time = time.time()
    agent = create_base_agent(inputs = 100, outputs = 100, meta_generation="test", generation=1)
    agent.save()
    return print("Total Time: "+str(round(time.time()-start_time,2))+"s")


main()
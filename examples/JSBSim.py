from argparse import ArgumentParser

from PyJSBSim import FGFDMExec, FGTrim

def get_arguments():
    parser = ArgumentParser(description="JSBSim wrapper demo")
    
    parser.add_argument("jsbsim_path", action="store", help="Path to JSBSim source code")
    parser.add_argument("script", action="store", help="script name")

    return parser.parse_args()

def main():
    args = get_arguments()
    
    fdmexec = FGFDMExec()
    
    fdmexec.SetRootDir(args.jsbsim_path)
    fdmexec.SetAircraftPath("aircraft")
    fdmexec.SetEnginePath("engine")
    fdmexec.SetSystemsPath("systems")
    
    fdmexec.Setdt(1.0/60.0)
    
    script_loaded = fdmexec.LoadScript(args.script, 1.0/60.0, "")
    
    if not script_loaded:
        print("Failed to load script")
        exit(-1)
    
    ic_has_run = fdmexec.RunIC()
    
    if not ic_has_run:
        print("Failed to run initial condition")
        exit(-1)
    
    fdmexec.PrintSimulationConfiguration()
    
    fdmexec.GetPropagate().DumpState()
    
    if fdmexec.GetIC().NeedTrim():
        trimmer = FGTrim(fdmexec)
        trim_result = trimmer.DoTrim()
        if not trim_result:
            print("Failed to trim aircraft")
            exit(-1)
    
    initial_run = fdmexec.Run()
    
    if not initial_run:
        print("Failed to make initial run")
        exit(-1)
        
    running = True
    while running:
        fdmexec.ProcessMessage()
        fdmexec.CheckIncrementalHold()
        running = fdmexec.Run()
        
    fdmexec.PrintPropertyCatalog()

if __name__ == "__main__":
    main()
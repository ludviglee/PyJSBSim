from argparse import ArgumentParser
import csv

from PyJSBSim import FGFDMExec, tFull


def get_arguments():
    parser = ArgumentParser(description="C172P demo")

    parser.add_argument("jsbsim_path",
                        help="the path to the JSBSim source code")

    return parser.parse_args()


def main():
    args = get_arguments()

    fdmexec = FGFDMExec()

    fdmexec.SetRootDir(args.jsbsim_path)
    fdmexec.SetAircraftPath("aircraft")
    fdmexec.SetEnginePath("engine")
    fdmexec.SetSystemsPath("systems")

    fdmexec.Setdt(1.0 / 60.0)

    fdmexec.LoadModel("c172p")

    fdmexec.GetIC().Load("reset01")

    fdmexec.RunIC()

    fdmexec.SetPropertyValue("propulsion/starter_cmd", 1.0)
    fdmexec.SetPropertyValue("propulsion/magneto_cmd", 3.0)
    fdmexec.SetPropertyValue("fcs/throttle-cmd-norm", 0.15)
    fdmexec.SetPropertyValue("fcs/mixture-cmd-norm", 1.0)

    fdmexec.DoTrim(tFull)

    fdmexec.Run()

    run_until = fdmexec.GetSimTime() + 5.0

    field_names = [
        "time",
        "u_dot", "v_dot", "w_dot",
        "p_dot", "q_dot", "r_dot"
        "x_moment", "y_moment", "z_moment",
        "x_force", "y_force", "z_force",
        "u", "v", "w",
        "p", "q", "r",
        "phi", "theta", "psi",
        "latitude", "longitude", "altitude",
        "v_cal", "v_equ", "v_true",
        "pressure", "temperature"
    ]

    with open("flight_data.csv", "w") as f:
        csv_writer = csv.writer(f, delimiter=",")
        csv_writer.writerow(field_names)

        while fdmexec.GetSimTime() < run_until:
            fdmexec.Run()

            data = [
                fdmexec.GetSimTime(),
                fdmexec.GetAccelerations().GetUVWdot(1),
                fdmexec.GetAccelerations().GetUVWdot(2),
                fdmexec.GetAccelerations().GetUVWdot(3),
                fdmexec.GetAccelerations().GetPQRdot(1),
                fdmexec.GetAccelerations().GetPQRdot(2),
                fdmexec.GetAccelerations().GetPQRdot(3),
                fdmexec.GetAccelerations().GetMoments(1),
                fdmexec.GetAccelerations().GetMoments(2),
                fdmexec.GetAccelerations().GetMoments(3),
                fdmexec.GetAccelerations().GetForces(1),
                fdmexec.GetAccelerations().GetForces(2),
                fdmexec.GetAccelerations().GetForces(3),
                fdmexec.GetPropagate().GetUVW(1),
                fdmexec.GetPropagate().GetUVW(2),
                fdmexec.GetPropagate().GetUVW(3),
                fdmexec.GetPropagate().GetPQR(1),
                fdmexec.GetPropagate().GetPQR(2),
                fdmexec.GetPropagate().GetPQR(3),
                fdmexec.GetPropagate().GetEuler(1),
                fdmexec.GetPropagate().GetEuler(2),
                fdmexec.GetPropagate().GetEuler(3),
                fdmexec.GetPropagate().GetLatitudeDeg(),
                fdmexec.GetPropagate().GetLongitudeDeg(),
                fdmexec.GetPropagate().GetAltitudeASL(),
                fdmexec.GetAuxiliary().GetVcalibratedKTS(),
                fdmexec.GetAuxiliary().GetVequivalentKTS(),
                fdmexec.GetAuxiliary().GetVtrueKTS(),
                fdmexec.GetAuxiliary().GetTotalPressure(),
                fdmexec.GetAuxiliary().GetTotalTemperature()
            ]

            csv_writer.writerow(data)


if __name__ == "__main__":
    main()

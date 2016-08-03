%module PyJSBSim
%{
#include <JSBSim/FGJSBBase.h>
#include <JSBSim/math/FGMatrix33.h>
#include <JSBSim/math/FGColumnVector3.h>
#include <JSBSim/math/FGQuaternion.h>
#include <JSBSim/math/FGLocation.h>
#include <JSBSim/models/FGModel.h>
#include <JSBSim/initialization/FGInitialCondition.h>
#include <JSBSim/input_output/FGPropertyManager.h>
#include <JSBSim/models/FGPropagate.h>
#include <JSBSim/models/FGAtmosphere.h>
#include <JSBSim/models/FGAccelerations.h>
#include <JSBSim/models/FGSurface.h>
#include <JSBSim/models/FGLGear.h>
#include <JSBSim/models/FGFCS.h>
#include <JSBSim/models/propulsion/FGThruster.h>
#include <JSBSim/models/propulsion/FGEngine.h>
#include <JSBSim/models/FGPropulsion.h>
#include <JSBSim/models/FGMassBalance.h>
#include <JSBSim/math/FGFunction.h>
#include <JSBSim/models/FGAerodynamics.h>
#include <JSBSim/models/FGInertial.h>
#include <JSBSim/models/FGPropagate.h>
#include <JSBSim/models/FGAuxiliary.h>
#include <JSBSim/models/FGOutput.h>
#include <JSBSim/models/FGAircraft.h>
#include <JSBSim/FGFDMExec.h>
#include <JSBSim/initialization/FGTrimAxis.h>
#include <JSBSim/initialization/FGTrim.h>
%}

%exception DoTrim {
   try {
      $action
   } catch (char const* e) {
      PyErr_SetString(PyExc_Exception, e);
      return NULL;
   }
}

%include "std_string.i"
%include "std_vector.i"

namespace std
{
  %template(FGFunctionVector) vector<JSBSim::FGFunction*>;
}

%ignore JSBSim::FGFDMExec::GetGroundCallback;
%ignore JSBSim::FGFDMExec::SetGroundCallback;
%ignore JSBSim::FGFDMExec::GetChildFDM;
%ignore JSBSim::FGLocation::GetGroundCallback;
%ignore JSBSim::FGLocation::SetGroundCallback;
%ignore JSBSim::FGAircraft::unbind;

%include <JSBSim/FGJSBBase.h>
%include <JSBSim/math/FGMatrix33.h>
%include <JSBSim/math/FGColumnVector3.h>
%include <JSBSim/math/FGQuaternion.h>
%include <JSBSim/math/FGLocation.h>
%include <JSBSim/models/FGModel.h>
%include <JSBSim/initialization/FGInitialCondition.h>
%include "jsbsim_wrapper/FGPropertyManager.h"
%include <JSBSim/models/FGPropagate.h>
%include <JSBSim/models/FGAtmosphere.h>
%include <JSBSim/models/FGAccelerations.h>
%include <JSBSim/models/FGSurface.h>
%include <JSBSim/models/FGLGear.h>
%include <JSBSim/models/FGFCS.h>
%include <JSBSim/models/propulsion/FGThruster.h>
%include <JSBSim/models/propulsion/FGEngine.h>
%include <JSBSim/models/FGPropulsion.h>
%include <JSBSim/models/FGMassBalance.h>
%include <JSBSim/math/FGFunction.h>
%include <JSBSim/models/FGAerodynamics.h>
%include <JSBSim/models/FGInertial.h>
%include <JSBSim/models/FGPropagate.h>
%include <JSBSim/models/FGAuxiliary.h>
%include <JSBSim/models/FGOutput.h>
%include <JSBSim/models/FGAircraft.h>
%include <JSBSim/FGFDMExec.h>
%include <JSBSim/initialization/FGTrimAxis.h>
%include <JSBSim/initialization/FGTrim.h>

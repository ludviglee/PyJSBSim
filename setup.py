from setuptools import setup, Extension

jsbsim_wrapper_extension = Extension("_PyJSBSim",
                                     include_dirs=[ 
                                                   "/usr/local/include", 
                                                   "/usr/local/include/JSBSim",
                                                   ],
                                     sources=["PyJSBSim.i"],
                                     library_dirs=["/usr/local/lib"],
                                     libraries=["JSBSim"],
                                     swig_opts=['-c++',
                                                '-I/usr/local/include']
                                     )

setup(name="PyJSBSim",
      version = '0.0.1',
      description = 'JSBSim wrapper',
      author = 'Panagiotis Matigakis',
      author_email = 'pmatigakis@gmail.com',
      ext_modules=[jsbsim_wrapper_extension],
      py_modules=["PyJSBSim"])
#!/usr/local/bin/python
#-----------------------------------------------------------------||||||||||||--
# Name:          setup/py
# Purpose:       install
#
# Authors:       Christopher Ariza
#
# License:       GPL
#-----------------------------------------------------------------||||||||||||--

import sys, os
from martingale import info



descriptionShort = 'Tools for live electronics and real-time computer music performance in Pure Data (Pd)'

descriptionLong = '''Martingale provides a high-level library of cross-platform Pure Data (Pd) abstractions for quickly and easily creating complex real-time instruments and signal processors.

Numerous examples of creating real-time performance instruments are given, employing interfaces built with game pads, iPod/iPad (TouchOSC), and MIDI instruments. 

A core-library of tools provides ready-to-play instruments built around a common abstraction of a dual-analog game pad. Any of a number of similar game-pad devices (including the Logitech Dual Action, Logitech ChillStream, and Sony Sixaxis) can be employed with the same instruments, providing uniform access for musicians with diverse platforms and hardware.

Martingale is built upon the cross platform Pd-extended distribution.
'''

def _getPackagesList():
    """list of all packages, delimited by period"""
    pkg = (  'martingale', 
             'martingale.audio', 
             'martingale.compositions', 
             'martingale.compositions.arizaWork01', 
             'martingale.compositions.arizaWork02', 
             'martingale.compositions.arizaWork03', 
             'martingale.interfaces', 
             'martingale.interfaces.touchosc', 
             'martingale.interfaces.dangerShield', 
             'martingale.pd', 
             'martingale.pd.apps', 
             'martingale.pd.demo', 
             'martingale.pd.docs', 
             'martingale.pd.externals', 
             'martingale.pd.externals.win', 
             'martingale.pd.instruments', 
             'martingale.pd.instruments.dangerShield', 
             'martingale.pd.instruments.dualAnalogChillStream', 
             'martingale.pd.instruments.dualAnalogChillStream.mono', 
             'martingale.pd.instruments.dualAnalogChillStream.poly', 
             'martingale.pd.instruments.dualAnalogJoystick', 
             'martingale.pd.instruments.dualAnalogJoystick.mono', 
             'martingale.pd.instruments.dualAnalogJoystick.poly', 
             'martingale.pd.instruments.dualAnalogRoot', 
             'martingale.pd.instruments.dualAnalogRoot.mono', 
             'martingale.pd.instruments.dualAnalogRoot.poly', 
             'martingale.pd.instruments.dualAnalogSixaxis', 
             'martingale.pd.instruments.dualAnalogSixaxis.mono', 
             'martingale.pd.instruments.dualAnalogSixaxis.poly', 
             'martingale.pd.instruments.dualAnalogVirtual', 
             'martingale.pd.instruments.dualAnalogVirtual.mono', 
             'martingale.pd.instruments.dualAnalogVirtual.poly', 
             'martingale.pd.instruments.midi', 
             'martingale.pd.instruments.nanoKey', 
             'martingale.pd.instruments.touchosc', 
             'martingale.pd.instruments.touchosc.mono', 
             'martingale.pd.instruments.touchosc.poly', 
             'martingale.pd.lib', 
             'martingale.py', 
             'martingale.py.demo', 
             'martingale.sc', 
             'martingale.sc.demo', 
             )
    return pkg

def _getPackageData():
    pkgData = [
             'audio/*.aif',
             'compositions/arizaWork01/*.txt',
             'compositions/arizaWork01/*.pd',
             'compositions/arizaWork02/*.txt',
             'compositions/arizaWork02/*.pd',
             'compositions/arizaWork03/*.txt',
             'compositions/arizaWork03/*.pd',

             'interfaces/touchosc/*.png',
             'interfaces/touchosc/*.touchosc',
             'interfaces/touchosc/*.py',

             'interfaces/dangerShield/*.pde',
             'interfaces/dangerShield/*.py',

             'pd/apps/*.pd', 
             'pd/demo/*.pd', 
             'pd/docs/*.pd', 
             'pd/docs/externals/win/*.pd', 
             'pd/docs/*.pdf', 
             'pd/instruments/*.pd', 
             'pd/instruments/*.py', 

             'pd/instruments/dangerShield/*.pd', 
             'pd/instruments/dangerShield/*.py', 

             'pd/instruments/dualAnalogChillStream/*.pd', 
             'pd/instruments/dualAnalogChillStream/*.py', 
             'pd/instruments/dualAnalogChillStream/mono/*.pd', 
             'pd/instruments/dualAnalogChillStream/mono/*.py', 
             'pd/instruments/dualAnalogChillStream/poly/*.pd', 
             'pd/instruments/dualAnalogChillStream/poly/*.py', 
             'pd/instruments/dualAnalogChillStream/poly/*.pdf', 

             'pd/instruments/dualAnalogJoystick/*.pd', 
             'pd/instruments/dualAnalogJoystick/*.py', 
             'pd/instruments/dualAnalogJoystick/mono/*.pd', 
             'pd/instruments/dualAnalogJoystick/mono/*.py', 
             'pd/instruments/dualAnalogJoystick/poly/*.pd', 
             'pd/instruments/dualAnalogJoystick/poly/*.py', 
             'pd/instruments/dualAnalogJoystick/poly/*.pdf', 

             'pd/instruments/dualAnalogRoot/*.pd', 
             'pd/instruments/dualAnalogRoot/*.py', 
             'pd/instruments/dualAnalogRoot/mono/*.pd', 
             'pd/instruments/dualAnalogRoot/mono/*.py', 
             'pd/instruments/dualAnalogRoot/poly/*.pd', 
             'pd/instruments/dualAnalogRoot/poly/*.py', 
             'pd/instruments/dualAnalogRoot/poly/*.pdf', 

             'pd/instruments/dualAnalogSixaxis/*.pd', 
             'pd/instruments/dualAnalogSixaxis/*.py', 
             'pd/instruments/dualAnalogSixaxis/mono/*.pd', 
             'pd/instruments/dualAnalogSixaxis/mono/*.py', 
             'pd/instruments/dualAnalogSixaxis/poly/*.pd', 
             'pd/instruments/dualAnalogSixaxis/poly/*.py', 
             'pd/instruments/dualAnalogSixaxis/poly/*.pdf', 

             'pd/instruments/dualAnalogVirtual/*.pd', 
             'pd/instruments/dualAnalogVirtual/*.py', 
             'pd/instruments/dualAnalogVirtual/mono*.pd', 
             'pd/instruments/dualAnalogVirtual/mono/*.py', 
             'pd/instruments/dualAnalogVirtual/poly/*.pd', 
             'pd/instruments/dualAnalogVirtual/poly/*.py', 
             'pd/instruments/dualAnalogVirtual/poly/*.pdf', 

             'pd/instruments/midi/*.pd', 
             'pd/instruments/midi/*.py', 

             'pd/instruments/nanoKey/*.pd', 
             'pd/instruments/nanoKey/*.py', 

             'pd/instruments/touchosc/*.pd', 
             'pd/instruments/touchosc/*.py', 
             'pd/instruments/touchosc/mono/*.pd', 
             'pd/instruments/touchosc/mono/*.py', 
             'pd/instruments/touchosc/poly/*.pd', 
             'pd/instruments/touchosc/poly/*.py', 

             'pd/lib/*.pd', 
             'pd/lib/*.txt', 
             'py/demo/*.tiff', 
             'sc/demo/*.scd', 

    ] 
    return pkgData


def _getClassifiers():
    classifiers = [
            # 'Development Status :: 5 - Production/Stable',
            # 'Environment :: Console',
             'Intended Audience :: End Users/Desktop',
             'Intended Audience :: Developers',
            # 'License :: OSI Approved :: GNU General Public License (GPL)',
             'Natural Language :: English', 
             'Operating System :: MacOS',
             'Operating System :: Microsoft :: Windows',
             'Operating System :: POSIX',
             'Operating System :: OS Independent',
             'Programming Language :: Python',
             'Topic :: Multimedia :: Sound/Audio',
             'Topic :: Artistic Software',
             ]
    return classifiers
     


def writeManifestTemplate(fpPackageDir):
    dst = os.path.join(fpPackageDir, 'MANIFEST.in')
    msg = []
    msg.append('prune dist\n')
    msg.append('global-include *.txt *.xml *.pd *.aif *.pdf *.html *.touchosc *.png *.dll *.pde \n')

    f = open(dst, 'w')
    f.writelines(msg)
    f.close()



def runDisutils(bdistType):
    if bdistType == 'bdist_egg':
        print('using setuptools')
        from setuptools import setup
    else:
        from distutils.core import setup
    # store object for later examination
    pkgData = _getPackageData()
    setup(name = 'martingale', 
        version = info.VERSION_STR,
        description = descriptionShort, 
        long_description =  descriptionLong,
        author = 'Christopher Ariza, others',
        #author_email = '',
        license = 'GPL', 
        #url = '',
        classifiers = _getClassifiers(),
        download_url = 'http://googlecode/com/files/martingale-%s/tar/gz' % info.VERSION_STR,
        packages = _getPackagesList(), 
        package_data = {'martingale' : pkgData}
    ) # close setup args
    
        


if sys.argv[1] in ['sdist']:

# if sys/argv[1] in ['bdist', 'sdist', 'register', 'bdist_mpkg',
#                         'bdist_rpm', 'bdist_deb', 'bdist_wininst',
#                         'bdist_egg']:

    fpMartingale = os.path.dirname(info.__file__) # list, get first item
    fpPackageDir = os.path.dirname(fpMartingale)

    print('fpPackageDir = %s' % fpPackageDir)
    writeManifestTemplate(fpPackageDir)
    runDisutils(sys.argv[1])
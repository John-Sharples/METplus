***************************
METplus Release Information
***************************

.. _release-notes:

Users can view the :ref:`releaseCycleStages` section of
the Release Guide for descriptions of the development releases (including
beta releases and release candidates), official releases, and bugfix
releases for the METplus Components.

.. _components-release-notes:

METplus Components Release Note Links
=====================================

* MET (`latest <https://met.readthedocs.io/en/latest/Users_Guide/release-notes.html>`__, `development <https://met.readthedocs.io/en/develop/Users_Guide/release-notes.html>`__)
* METviewer (`latest <https://metviewer.readthedocs.io/en/latest/Users_Guide/release-notes.html>`__, `development <https://metviewer.readthedocs.io/en/develop/Users_Guide/release-notes.html>`__)
* METplotpy (`latest <https://metplotpy.readthedocs.io/en/latest/Users_Guide/release-notes.html>`__, `development <https://metplotpy.readthedocs.io/en/develop/Users_Guide/release-notes.html>`__)
* METcalcpy (`latest <https://metcalcpy.readthedocs.io/en/latest/Users_Guide/release-notes.html>`__, `development <https://metcalcpy.readthedocs.io/en/develop/Users_Guide/release-notes.html>`__)
* METdataio (`latest <https://metdataio.readthedocs.io/en/latest/Users_Guide/release-notes.html>`__, `development <https://metdataio.readthedocs.io/en/develop/Users_Guide/release-notes.html>`__)
* METexpress (`latest <https://github.com/dtcenter/METexpress/releases>`__, `development <https://github.com/dtcenter/METexpress/releases>`__)
* METplus Wrappers (`latest <https://metplus.readthedocs.io/en/latest/Users_Guide/release-notes.html>`__, :ref:`upgrade instructions <upgrade-instructions>`, `development <https://metplus.readthedocs.io/en/develop/Users_Guide/release-notes.html>`__)


METplus Wrappers Release Notes
==============================

When applicable, release notes are followed by the
`GitHub issue <https://github.com/dtcenter/METplus/issues>`__ number which
describes the bugfix, enhancement, or new feature.

METplus Version 5.0.2 Release Notes (2023-06-02)
------------------------------------------------

* Bugfixes:

  * Define the order of the forecast variables numerically rather than alphabetically
    (`#2070 <https://github.com/dtcenter/METplus/issues/2070>`_)
  * Allow setting of convert, censor_thresh, and censor_val in regrid dictionary
    (`#2082 <https://github.com/dtcenter/METplus/issues/2082>`_)
  * Skip-if-output-exists logic incorrectly skips files
    (`#2096 <https://github.com/dtcenter/METplus/issues/2096>`_)
  * Prevent error if no commands were run because they were skipped
    (`#2098 <https://github.com/dtcenter/METplus/issues/2098>`_)
  * Allow spaces for complex categorical thresholds
    (`#2189 <https://github.com/dtcenter/METplus/issues/2189>`_)


METplus Version 5.0.1 Release Notes (2023-02-27)
------------------------------------------------

* Bugfixes:

  * StatAnalysis - allow run once for each valid time
    (`#2026 <https://github.com/dtcenter/METplus/issues/2026>`_)

* Internal:

  * Add modulefiles to the repository
    (`#2015 <https://github.com/dtcenter/METplus/issues/2015>`_)

* Documentation:

  * Update the METplus Components Python Requirements Documentation
    (`#2016 <https://github.com/dtcenter/METplus/issues/2016>`_)


METplus Version 5.0.0 Release Notes (2022-12-09)
------------------------------------------------

.. warning:: **MAJOR CHANGES**:

  * The LOOP_ORDER config variable was removed. The variable set in a user's
    config file will be ignored in favor of executing the logic that
    corresponds to *LOOP_ORDER = processes*, where all times are processed for
    the first item in the PROCESS_LIST, then all times are processed for the
    second item in the PROCESS_LIST, etc. This may change the order that
    commands are executed in a use case, but it should not change the results.
  * The METplus Dockerfile was moved to internal/scripts/docker.
    It was previously found in scripts/docker.
  * Use cases that include **EnsembleStat** wrapper will require config file
    updates. See :ref:`upgrade-instructions`.
  * The default value of :term:`SCRUB_STAGING_DIR` is now *True*.
    This means some intermediate files that are auto-generated by METplus such
    as file lists and uncompressed files will automatically be removed unless
    this option is set by the user.
    These files are typically only used to debug unexpected issues.
  * The default value of :term:`METPLUS_CONF` now includes the
    :term:`LOG_TIMESTAMP` so each METplus run will generate a unique final
    config file, e.g. metplus_final.conf.20220921121733.


* Enhancements:

  * **Enhance MODE wrapper to support multi-variate MODE**
    (`#1585 <https://github.com/dtcenter/METplus/issues/1585>`_)
  * **Allow FCST_IS_PROB variable setting specific to tool
    (FCST_<tool_name>_IS_PROB)**
    (`#1586 <https://github.com/dtcenter/METplus/issues/1586>`_)
  * **Enhance climatology field settings to be consistent with fcst/obs field**
    (`#1599 <https://github.com/dtcenter/METplus/issues/1599>`_)
  * Update Hovmoeller Use case to use updated Hovmoeller plotting
    (`#1650 <https://github.com/dtcenter/METplus/issues/1650>`_)
  * **Update the EnsembleStat wrapper and use case examples to remove
    ensemble post processing logic**
    (`#1816 <https://github.com/dtcenter/METplus/issues/1816>`_)
  * Enhance logic to consistently create directories
    (`#1657 <https://github.com/dtcenter/METplus/issues/1657>`_)
  * Create checksum for released code
    (`#262 <https://github.com/dtcenter/METplus/issues/262>`_)
  * Add the user ID to the log output at beginning and end of each
    METplus wrappers run
    (`dtcenter/METplus-Internal#20 <https://github.com/dtcenter/METplus-Internal/issues/20>`_)
  * Update logic to name final conf and intermediate files with a unique
    identifier
    (`dtcenter/METplus-Internal#32 <https://github.com/dtcenter/METplus-Internal/issues/32>`_)
  * Change default logging time information
    (`dtcenter/METplus-Internal#34 <https://github.com/dtcenter/METplus-Internal/issues/34>`_)
  * **Remove LOOP_ORDER config variable**
    (`#1687 <https://github.com/dtcenter/METplus/issues/1687>`_)
  * **Add unique identifier for each METplus run to configuration**
    (`#1829 <https://github.com/dtcenter/METplus/issues/1829>`_)
  * StatAnalysis - Support setting multiple jobs
    (`#1842 <https://github.com/dtcenter/METplus/issues/1842>`_)
  * StatAnalysis - Set MET verbosity
    (`#1772 <https://github.com/dtcenter/METplus/issues/1772>`_)
  * StatAnalysis - Support using both init/valid variables in
    string substitution
    (`#1861 <https://github.com/dtcenter/METplus/issues/1861>`_)
  * StatAnalysis - Allow filename template tags in jobs
    (`#1862 <https://github.com/dtcenter/METplus/issues/1862>`_)
  * StatAnalysis - Support looping over groups of list items
    (`#1870 <https://github.com/dtcenter/METplus/issues/1870>`_)
  * StatAnalysis - Allow processing of time ranges other than daily
    (`#1871 <https://github.com/dtcenter/METplus/issues/1871>`_)
  * StatAnalysis - Add support for using a custom loop list
    (`#1893 <https://github.com/dtcenter/METplus/issues/1893>`_)
  * Remove MakePlots wrapper
    (`#1843 <https://github.com/dtcenter/METplus/issues/1843>`_)
  * Add support in EnsembleStat wrapper for setting -ens_mean
    command line argument
    (`#1569 <https://github.com/dtcenter/METplus/issues/1569>`_)
  * Enhance METplus to have better signal handling for shutdown events
    (`dtcenter/METplus-Internal#27 <https://github.com/dtcenter/METplus-Internal/issues/27>`_)
  * TCPairs and TCStat - add support for new config options and
    command line arguments
    (`#1898 <https://github.com/dtcenter/METplus/issues/1898>`_)
  * Enhance the GridStat and PointStat wrappers to handle the
    addition of SEEPS
    (`#1953 <https://github.com/dtcenter/METplus/issues/1953>`_)
  * SeriesAnalysis - add support for setting mask dictionary
    (`#1926 <https://github.com/dtcenter/METplus/issues/1926>`_)
  * Update Python requirement to 3.8.6
    (`#1566 <https://github.com/dtcenter/METplus/issues/1566>`_)
  * Enhance StatAnalysis wrapper to support now and today
    (`#1669 <https://github.com/dtcenter/METplus/issues/1669>`_)
  * **Clean up use case configuration files**
    (`#1402 <https://github.com/dtcenter/METplus/issues/1402>`_)
  * Add support for creating multiple input datasets
    (`#1694 <https://github.com/dtcenter/METplus/issues/1694>`_)

* Bugfixes:

  * PCPCombine - custom loop list does not work for subtract method
    (`#1884 <https://github.com/dtcenter/METplus/issues/1884>`_)
  * Set level properly in filename template for EnsembleStat forecast input
    (`#1910 <https://github.com/dtcenter/METplus/issues/1910>`_)
  * Prevent duplicate observation files using a file window if
    compressed equivalent files exist in same directory
    (`#1939 <https://github.com/dtcenter/METplus/issues/1939>`_)
  * Allow NA value for <TOOL-NAME>_CLIMO_[MEAN/STDEV]_HOUR_INTERVAL
    (`#1787 <https://github.com/dtcenter/METplus/issues/1787>`_)
  * Reconcile setting of METPLOTPY_BASE for use cases
    (`#1713 <https://github.com/dtcenter/METplus/issues/1713>`_)
  *  Add support for the {custom} loop string in the MODEL config variable
     (`#1382 <https://github.com/dtcenter/METplus/issues/1382>`_)
  *  Fix PCPCombine extra options removal of semi-colon
     (`#1534 <https://github.com/dtcenter/METplus/issues/1534>`_)
  *  Fix reset of arguments for some wrappers
     (i.e. GenEnsProd) after each run
     (`#1555 <https://github.com/dtcenter/METplus/issues/1555>`_)
  *  Enhance METDbLoad Wrapper to find MODE .txt files
     (`#1608 <https://github.com/dtcenter/METplus/issues/1608>`_)
  *  Add missing brackets around list variable values for StatAnalysis wrapper
     (`#1641 <https://github.com/dtcenter/METplus/issues/1641>`_)
  *  Allow NA value for <TOOL-NAME>_CLIMO_[MEAN/STDEV]_DAY_INTERVAL
     (`#1653 <https://github.com/dtcenter/METplus/issues/1653>`_)

* New Wrappers:

  * PlotPointObs
    (`#1489 <https://github.com/dtcenter/METplus/issues/1489>`_)

* New Use Cases:

  * PANDA-C use cases
    (`#1686 <https://github.com/dtcenter/METplus/issues/1686>`_)
  * MJO-ENSO diagnostics
    (`#1330 <https://github.com/dtcenter/METplus/issues/1330>`_)
  * Probability of Exceedence for 85th percentile temperatures
    (`#1808 <https://github.com/dtcenter/METplus/issues/1808>`_)
  * FV3 Physics Tendency plotting via METplotpy
    (`#1852 <https://github.com/dtcenter/METplus/issues/1852>`_)
  * StatAnalysis Python Embedding using IODA v2.0
    (`#1453 <https://github.com/dtcenter/METplus/issues/1453>`_)
  * StatAnalysis Python Embedding to read native grid (u-grid)
    (`#1561 <https://github.com/dtcenter/METplus/issues/1561>`_)

* Documentation:

  * Update documentation to include instructions
    to disable UserScript wrapper
    (`dtcenter/METplus-Internal#33 <https://github.com/dtcenter/METplus-Internal/issues/33>`_)

* Internal:

  * Organize utility scripts used by multiple wrappers
    (`#344 <https://github.com/dtcenter/METplus/issues/344>`_)
  * Fix GitHub Actions warnings - update the version of actions
    and replace set-output
    (`#1863 <https://github.com/dtcenter/METplus/issues/1863>`_)
  * Update diff logic to handle CSV files that have rounding differences
    (`#1865 <https://github.com/dtcenter/METplus/issues/1865>`_)
  * Add unit tests for expected failure
    (`dtcenter/METplus-Internal#24 <https://github.com/dtcenter/METplus-Internal/issues/24>`_)
  * Add instructions in Release Guide for "Recreate an Existing Release"
    (`#1746 <https://github.com/dtcenter/METplus/issues/1746>`_)
  * Add modulefiles used for installations on various machines
    (`#1749 <https://github.com/dtcenter/METplus/issues/1749>`_)
  * Document GitHub Discussions procedure for the Contributor's Guide
    (`#1159 <https://github.com/dtcenter/METplus/issues/1159>`_)
  * Create a METplus "Release Guide" describing how to build
    releases for the METplus components
    (`#673 <https://github.com/dtcenter/METplus/issues/673>`_)
  * Update documentation about viewing RTD URLs on branches
    (`#1512 <https://github.com/dtcenter/METplus/issues/1512>`_)


.. _upgrade-instructions:
    
METplus Wrappers Upgrade Instructions
=====================================

EnsembleStat/GenEnsProd
-----------------------

.. note::

    If :ref:`ensemble_stat_wrapper` is not found in the :term:`PROCESS_LIST`
    for any use cases, then this section is not relevant.

The METplus v5.0.0 coordinated release includes changes that remove ensemble
product generation from EnsembleStat. GenEnsProd is now required to generate
ensemble products. There are 3 situations listed below that require slightly
different modifications:

* :ref:`upgrade-ensemble-case1`
* :ref:`upgrade-ensemble-case2`
* :ref:`upgrade-ensemble-case3`

.. _upgrade-ensemble-case1:

Case 1: EnsembleStat only generating ensemble products
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the use case had been calling EnsembleStat **WITHOUT** the **-grid_obs** or
**-point_obs** command line options, we can assume it was only doing ensemble
post-processing.
That call to EnsembleStat should be replaced with a call to
GenEnsProd instead.

Rename Variables
""""""""""""""""

.. role:: raw-html(raw)
   :format: html

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Old Name
     - New Name
   * - FCST_ENSEMBLE_STAT_INPUT_DIR
     - GEN_ENS_PROD_INPUT_DIR
   * - FCST_ENSEMBLE_STAT_INPUT_TEMPLATE
     - GEN_ENS_PROD_INPUT_TEMPLATE
   * - ENSEMBLE_STAT_OUTPUT_DIR
     - GEN_ENS_PROD_OUTPUT_DIR
   * - ENSEMBLE_STAT_OUTPUT_TEMPLATE
     - GEN_ENS_PROD_OUTPUT_TEMPLATE :raw-html:`<br />`
       **and add filename, see** :ref:`below<upgrade-ensemble-case1-filename>`
   * - ENSEMBLE_STAT_N_MEMBERS
     - GEN_ENS_PROD_N_MEMBERS
   * - ENSEMBLE_STAT_ENS_THRESH
     - GEN_ENS_PROD_ENS_THRESH
   * - ENSEMBLE_STAT_ENS_VLD_THRESH
     - GEN_ENS_PROD_VLD_THRESH
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_LATLON
     - GEN_ENS_PROD_ENSEMBLE_FLAG_LATLON
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_MEAN
     - GEN_ENS_PROD_ENSEMBLE_FLAG_MEAN
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_STDEV
     - GEN_ENS_PROD_ENSEMBLE_FLAG_STDEV
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_MINUS
     - GEN_ENS_PROD_ENSEMBLE_FLAG_MINUS
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_PLUS
     - GEN_ENS_PROD_ENSEMBLE_FLAG_PLUS
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_MIN
     - GEN_ENS_PROD_ENSEMBLE_FLAG_MIN
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_MAX
     - GEN_ENS_PROD_ENSEMBLE_FLAG_MAX
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_RANGE
     - GEN_ENS_PROD_ENSEMBLE_FLAG_RANGE
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_VLD_COUNT
     - GEN_ENS_PROD_ENSEMBLE_FLAG_VLD_COUNT
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_FREQUENCY
     - GEN_ENS_PROD_ENSEMBLE_FLAG_FREQUENCY
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_NEP
     - GEN_ENS_PROD_ENSEMBLE_FLAG_NEP
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_NMEP
     - GEN_ENS_PROD_ENSEMBLE_FLAG_NMEP
   * - ENSEMBLE_STAT_REGRID_TO_GRID
     - GEN_ENS_PROD_REGRID_TO_GRID
   * - ENSEMBLE_STAT_REGRID_METHOD
     - GEN_ENS_PROD_REGRID_METHOD
   * - ENSEMBLE_STAT_REGRID_WIDTH
     - GEN_ENS_PROD_REGRID_WIDTH
   * - ENSEMBLE_STAT_REGRID_VLD_THRESH
     - GEN_ENS_PROD_REGRID_VLD_THRESH
   * - ENSEMBLE_STAT_REGRID_SHAPE
     - GEN_ENS_PROD_REGRID_SHAPE
   * - ENSEMBLE_STAT_NBRHD_PROB_WIDTH
     - GEN_ENS_PROD_NBRHD_PROB_WIDTH
   * - ENSEMBLE_STAT_NBRHD_PROB_SHAPE
     - GEN_ENS_PROD_NBRHD_PROB_SHAPE
   * - ENSEMBLE_STAT_NBRHD_PROB_VLD_THRESH
     - GEN_ENS_PROD_NBRHD_PROB_VLD_THRESH
   * - ENSEMBLE_STAT_NMEP_SMOOTH_VLD_THRESH
     - GEN_ENS_PROD_NMEP_SMOOTH_VLD_THRESH
   * - ENSEMBLE_STAT_NMEP_SMOOTH_SHAPE
     - GEN_ENS_PROD_NMEP_SMOOTH_SHAPE
   * - ENSEMBLE_STAT_NMEP_SMOOTH_METHOD
     - GEN_ENS_PROD_NMEP_SMOOTH_METHOD
   * - ENSEMBLE_STAT_NMEP_SMOOTH_WIDTH
     - GEN_ENS_PROD_NMEP_SMOOTH_WIDTH
   * - ENSEMBLE_STAT_NMEP_SMOOTH_GAUSSIAN_DX
     - GEN_ENS_PROD_NMEP_SMOOTH_GAUSSIAN_DX
   * - ENSEMBLE_STAT_NMEP_SMOOTH_GAUSSIAN_RADIUS
     - GEN_ENS_PROD_NMEP_SMOOTH_GAUSSIAN_RADIUS

.. _upgrade-ensemble-case1-filename:

Set GenEnsProd output template to include filename
""""""""""""""""""""""""""""""""""""""""""""""""""

* **If the EnsembleStat output template was set**, then copy the value and add a
  template for the NetCDF output filename at the end following a forward slash
  ‘/’ character.

  For example, if

  .. code-block:: ini

     ENSEMBLE_STAT_OUTPUT_TEMPLATE = {valid?fmt=%Y%m%d%H}

  then set

  .. code-block:: ini

     GEN_ENS_PROD_OUTPUT_TEMPLATE = {valid?fmt=%Y%m%d%H}/gen_ens_prod_{valid?fmt=%Y%m%d_%H%M%S}V_ens.nc

  or something similar.

* **If the EnsembleStat output template was not set,** then set GenEnsProd’s
  template to the desired NetCDF output filename.

  Example:

  .. code-block:: ini

     GEN_ENS_PROD_OUTPUT_TEMPLATE = gen_ens_prod_{valid?fmt=%Y%m%d_%H%M%S}V_ens.nc

**Ensure that any downstream wrappers in the PROCESS_LIST are configured
to read the correct GenEnsProd output file instead of the _ens.nc file
that was previously generated by EnsembleStat.**

Handle ENS_VAR<n> variables
"""""""""""""""""""""""""""

**If ENS_VAR<n>_\* variables are already set,** this section can be skipped.

**If ENS_VAR<n>_\* variables are not set,** add ENS_VAR<n> variables.

*  If FCST/OBS verification is **NOT** being performed in the use case using another
   wrapper, then rename the FCST_VAR<n> variables to ENS_VAR<n>.

   For example:

   .. list-table::
      :widths: 50 50
      :header-rows: 1

      * - Old Name
	- New Name
      * - FCST_VAR1_NAME
        - ENS_VAR1_NAME
      * - FCST_VAR1_LEVELS
        - ENS_VAR1_LEVELS
      * - FCST_VAR2_NAME
        - ENS_VAR2_NAME
      * - FCST_VAR2_LEVELS
        - ENS_VAR2_LEVELS

     
*  If FCST/OBS verification is being performed by another tool, then add
   ENS_VAR<n> variables and set them equal to the corresponding
   FCST_VAR<n> values.

   For example:

  .. code-block:: ini

     ENS_VAR1_NAME = {FCST_VAR1_NAME}
     ENS_VAR1_LEVELS = {FCST_VAR1_LEVELS}
     ENS_VAR2_NAME = {FCST_VAR2_NAME}
     ENS_VAR2_LEVELS = {FCST_VAR2_LEVELS}

Remove Variables
""""""""""""""""

**Remove any remaining ENSEMBLE_STAT_\* variables that are no longer used.**

Some examples:

.. list-table::
   :widths: 50

   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_RANK
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_WEIGHT
   * - ENSEMBLE_STAT_MESSAGE_TYPE
   * - ENSEMBLE_STAT_OUTPUT_FLAG_ECNT
   * - ENSEMBLE_STAT_OUTPUT_FLAG_RPS
   * - ENSEMBLE_STAT_OUTPUT_FLAG_RHIST
   * - ENSEMBLE_STAT_OUTPUT_FLAG_PHIST
   * - ENSEMBLE_STAT_OUTPUT_FLAG_ORANK
   * - ENSEMBLE_STAT_OUTPUT_FLAG_SSVAR
   * - ENSEMBLE_STAT_OUTPUT_FLAG_RELP
   * - ENSEMBLE_STAT_OUTPUT_FLAG_PCT
   * - ENSEMBLE_STAT_OUTPUT_FLAG_PSTD
   * - ENSEMBLE_STAT_OUTPUT_FLAG_PJC
   * - ENSEMBLE_STAT_OUTPUT_FLAG_PRC
   * - ENSEMBLE_STAT_OUTPUT_FLAG_ECLV
   * - ENSEMBLE_STAT_DUPLICATE_FLAG
   * - ENSEMBLE_STAT_SKIP_CONST
   * - ENSEMBLE_STAT_OBS_ERROR_FLAG
   * - ENSEMBLE_STAT_ENS_SSVAR_BIN_SIZE
   * - ENSEMBLE_STAT_ENS_PHIST_BIN_SIZE
   * - ENSEMBLE_STAT_CI_ALPHA
   * - ENSEMBLE_STAT_MASK_GRID
   * - ENSEMBLE_STAT_MASK_POLY
   * - ENSEMBLE_STAT_INTERP_FIELD
   * - ENSEMBLE_STAT_INTERP_VLD_THRESH
   * - ENSEMBLE_STAT_INTERP_SHAPE
   * - ENSEMBLE_STAT_INTERP_METHOD
   * - ENSEMBLE_STAT_INTERP_WIDTH
   * - ENSEMBLE_STAT_OBS_QUALITY_INC/EXC
   * - ENSEMBLE_STAT_GRID_WEIGHT_FLAG

.. _upgrade-ensemble-case2:

Case 2: EnsembleStat performing ensemble verification but not generating ensemble products
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The use case will no longer generate a **_ens.nc** file and may create other
files (**_orank.nc** and **txt**) that contain requested output.

Rename Variables
""""""""""""""""

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Old Name
     - New Name
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_MEAN
     - ENSEMBLE_STAT_NC_ORANK_FLAG_MEAN
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_RANK
     - ENSEMBLE_STAT_NC_ORANK_FLAG_RANK
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_WEIGHT
     - ENSEMBLE_STAT_NC_ORANK_FLAG_WEIGHT
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_VLD_COUNT
     - ENSEMBLE_STAT_NC_ORANK_FLAG_VLD_COUNT

Remove Variables
""""""""""""""""

.. list-table::
   :widths: 50
		 
   * - All ENS_VAR<n>_* variables
   * - All ENSEMBLE_STAT_ENSEMBLE_FLAG_* variables
   * - ENSEMBLE_STAT_NBRHD_PROB_WIDTH
   * - ENSEMBLE_STAT_NBRHD_PROB_SHAPE
   * - ENSEMBLE_STAT_NBRHD_PROB_VLD_THRESH
   * - ENSEMBLE_STAT_NMEP_SMOOTH_VLD_THRESH
   * - ENSEMBLE_STAT_NMEP_SMOOTH_SHAPE
   * - ENSEMBLE_STAT_NMEP_SMOOTH_METHOD
   * - ENSEMBLE_STAT_NMEP_SMOOTH_WIDTH
   * - ENSEMBLE_STAT_NMEP_SMOOTH_GAUSSIAN_DX
   * - ENSEMBLE_STAT_NMEP_SMOOTH_GAUSSIAN_RADIUS

.. _upgrade-ensemble-case3:

Case 3: EnsembleStat generating ensemble products and performing ensemble verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add GenEnsProd to PROCESS_LIST
""""""""""""""""""""""""""""""

GenEnsProd will need to be added to the PROCESS_LIST in addition to
EnsembleStat to generate the ensemble verification output.

  .. code-block:: ini

     PROCESS_LIST = ..., EnsembleStat, GenEnsProd, ...

Set input variables
"""""""""""""""""""

Set the input dir and template variables for **GenEnsProd** to match
the values set for FCST input to EnsembleStat.
Also set the output dir to match EnsembleStat output dir.

  .. code-block:: ini

     GEN_ENS_PROD_INPUT_DIR = {FCST_ENSEMBLE_STAT_INPUT_DIR}
     GEN_ENS_PROD_INPUT_TEMPLATE = {FCST_ENSEMBLE_STAT_INPUT_TEMPLATE}
     GEN_ENS_PROD_OUTPUT_DIR = {ENSEMBLE_STAT_OUTPUT_DIR}

Set GenEnsProd output template to include filename
""""""""""""""""""""""""""""""""""""""""""""""""""

* **If the EnsembleStat output template is set**, then copy the value and add a
  template for the NetCDF output filename at the end following a forward slash
  ‘/’ character.

  For example, if

  .. code-block:: ini

     ENSEMBLE_STAT_OUTPUT_TEMPLATE = {valid?fmt=%Y%m%d%H}

  then set

  .. code-block:: ini

     GEN_ENS_PROD_OUTPUT_TEMPLATE = {valid?fmt=%Y%m%d%H}/gen_ens_prod_{valid?fmt=%Y%m%d_%H%M%S}V_ens.nc

  or something similar.

* **If the EnsembleStat output template is not set,** then set GenEnsProd’s
  template to the desired NetCDF output filename. Here is an example:

  .. code-block:: ini
		  
     GEN_ENS_PROD_OUTPUT_TEMPLATE = gen_ens_prod_{valid?fmt=%Y%m%d_%H%M%S}V_ens.nc

**Ensure that any downstream wrappers in the PROCESS_LIST are configured
to read the correct GenEnsProd output file instead of the _ens.nc file
that was previously generated by EnsembleStat.**

Handle ENS_VAR variables
""""""""""""""""""""""""

**If ENS_VAR<n>_\* variables are already set,** this section can be skipped.

**If ENS_VAR<n>_\* variables are not set,** add ENS_VAR<n> variables.

* If FCST_ENSEMBLE_STAT_VAR<n>_\* variables are set,
  set the ENS_VAR<n>_\* values to the same values.

  For example:

  .. code-block:: ini

     ENS_VAR1_NAME = {FCST_ENSEMBLE_STAT_VAR1_NAME}
     ENS_VAR1_LEVELS = {FCST_ENSEMBLE_STAT_VAR1_LEVELS}
     ENS_VAR2_NAME = {FCST_ENSEMBLE_STAT_VAR2_NAME}
     ENS_VAR2_LEVELS = {FCST_ENSEMBLE_STAT_VAR2_LEVELS}

* If FCST_ENSEMBLE_STAT_VAR<n>_\* variables are **not** set,
  set the ENS_VAR<n>_\* values to the values set for the FCST_VAR<n>_\*.

  For example:
 
  .. code-block:: ini

     ENS_VAR1_NAME = {FCST_VAR1_NAME}
     ENS_VAR1_LEVELS = {FCST_VAR1_LEVELS}
     ENS_VAR2_NAME = {FCST_VAR2_NAME}
     ENS_VAR2_LEVELS = {FCST_VAR2_LEVELS}

Set GenEnsProd Variables
""""""""""""""""""""""""

**If any of the following ENSEMBLE_STAT_\* variables are set in the
configuration file, then rename them to the corresponding
GEN_ENS_PROD_\* variable.
These are no longer valid settings for EnsembleStat.**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Old Name
     - New Name
   * - ENSEMBLE_STAT_NBRHD_PROB_WIDTH
     - GEN_ENS_PROD_NBRHD_PROB_WIDTH
   * - ENSEMBLE_STAT_NBRHD_PROB_SHAPE
     - GEN_ENS_PROD_NBRHD_PROB_SHAPE
   * - ENSEMBLE_STAT_NBRHD_PROB_VLD_THRESH
     - GEN_ENS_PROD_NBRHD_PROB_VLD_THRESH
   * - ENSEMBLE_STAT_NMEP_SMOOTH_VLD_THRESH
     - GEN_ENS_PROD_NMEP_SMOOTH_VLD_THRESH
   * - ENSEMBLE_STAT_NMEP_SMOOTH_SHAPE
     - GEN_ENS_PROD_NMEP_SMOOTH_SHAPE
   * - ENSEMBLE_STAT_NMEP_SMOOTH_METHOD
     - GEN_ENS_PROD_NMEP_SMOOTH_METHOD
   * - ENSEMBLE_STAT_NMEP_SMOOTH_WIDTH
     - GEN_ENS_PROD_NMEP_SMOOTH_WIDTH
   * - ENSEMBLE_STAT_NMEP_SMOOTH_GAUSSIAN_DX
     - GEN_ENS_PROD_NMEP_SMOOTH_GAUSSIAN_DX
   * - ENSEMBLE_STAT_NMEP_SMOOTH_GAUSSIAN_RADIUS
     - GEN_ENS_PROD_NMEP_SMOOTH_GAUSSIAN_RADIUS

**If any of the following ENSEMBLE_STAT_\* variables are set in the
configuration file, then set the corresponding GEN_ENS_PROD_\*
variables to the same value or reference the ENSEMBLE_STAT_\* version.**

.. list-table::
   :widths: 50

   * - ENSEMBLE_STAT_N_MEMBERS
   * - ENSEMBLE_STAT_ENS_THRESH
   * - ENSEMBLE_STAT_REGRID_TO_GRID
   * - ENSEMBLE_STAT_REGRID_METHOD
   * - ENSEMBLE_STAT_REGRID_WIDTH
   * - ENSEMBLE_STAT_REGRID_VLD_THRESH
   * - ENSEMBLE_STAT_REGRID_SHAPE
   * - FCST_ENSEMBLE_STAT_INPUT_GRID_DATATYPE

Example:

  .. code-block:: ini

     GEN_ENS_PROD_N_MEMBERS = {ENSEMBLE_STAT_N_MEMBERS}
     GEN_ENS_PROD_ENS_THRESH = {ENSEMBLE_STAT_ENS_THRESH}
     GEN_ENS_PROD_REGRID_TO_GRID = {ENSEMBLE_STAT_REGRID_TO_GRID}
     GEN_ENS_PROD_REGRID_METHOD = {ENSEMBLE_STAT_REGRID_METHOD}
     GEN_ENS_PROD_REGRID_WIDTH = {ENSEMBLE_STAT_REGRID_WIDTH}
     GEN_ENS_PROD_REGRID_VLD_THRESH = {ENSEMBLE_STAT_REGRID_VLD_THRESH}
     GEN_ENS_PROD_REGRID_SHAPE = {ENSEMBLE_STAT_REGRID_SHAPE}
     GEN_ENS_PROD_INPUT_DATATYPE = {FCST_ENSEMBLE_STAT_INPUT_GRID_DATATYPE}

**If any of the following ENSEMBLE_STAT_ENSEMBLE_FLAG_\* variables are set
in the configuration file, then rename them to the corresponding
ENSEMBLE_STAT_NC_ORANK_FLAG_\* variables AND add the corresponding
GEN_ENS_PROD_ENSEMBLE_FLAG_\* variables with the same value.**

.. list-table::
   :widths: 50

   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_LATLON
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_MEAN
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_VLD_COUNT

For example, if

  .. code-block:: ini

     ENSEMBLE_STAT_ENSEMBLE_FLAG_LATLON = TRUE

then remove it and set

  .. code-block:: ini

     ENSEMBLE_STAT_NC_ORANK_FLAG_LATLON = TRUE
     GEN_ENS_PROD_ENSEMBLE_FLAG_LATLON = TRUE

Another example, if

  .. code-block:: ini

     ENSEMBLE_STAT_ENSEMBLE_FLAG_MEAN = FALSE

then remove it and set

  .. code-block:: ini

     ENSEMBLE_STAT_NC_ORANK_FLAG_MEAN = FALSE
     GEN_ENS_PROD_ENSEMBLE_FLAG_MEAN = FALSE

Rename Variables
""""""""""""""""

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Old Name
     - New Name
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_STDEV
     - GEN_ENS_PROD_ENSEMBLE_FLAG_STDEV
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_MINUS
     - GEN_ENS_PROD_ENSEMBLE_FLAG_MINUS
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_PLUS
     - GEN_ENS_PROD_ENSEMBLE_FLAG_PLUS
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_MIN
     - GEN_ENS_PROD_ENSEMBLE_FLAG_MIN
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_MAX
     - GEN_ENS_PROD_ENSEMBLE_FLAG_MAX
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_RANGE
     - GEN_ENS_PROD_ENSEMBLE_FLAG_RANGE
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_FREQUENCY
     - GEN_ENS_PROD_ENSEMBLE_FLAG_FREQUENCY
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_NEP
     - GEN_ENS_PROD_ENSEMBLE_FLAG_NEP
   * - ENSEMBLE_STAT_ENSEMBLE_FLAG_NMEP
     - GEN_ENS_PROD_ENSEMBLE_FLAG_NMEP

For further assistance, please navigate to the
`METplus Discussions <https://github.com/dtcenter/METplus/discussions>`_ page.

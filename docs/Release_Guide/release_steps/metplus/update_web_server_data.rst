Update DTC Web Server Data
--------------------------

Create Directory for Next Release
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the DTC web server where the sample input data for use cases is hosted,
run the setup_next_release_data.py script for the next upcoming release
to set up the data directory for the next major/minor version development.
The script can be found in the METplus repository in internal/tests/use_cases.
The file should be found in the home directory of the met_test user on
the DTC web server host. It is linked to the file in the METplus repository.
Pull the latest changes from the develop branch before running the script::

    runas met_test
    cd /home/met_test/METplus
    git checkout develop
    git pull

Now run the script passing in the version of the next release, i.e.
if creating the v4.1.0 release, pass in v5.0 as the argument::

    /home/met_test/setup_next_release_data.py v5.0

See the comments in the script for more details.
Ensure that the script runs without error and that the newly created
directory contains links to all of the sample data tar files::

    ls -lh /home/met_test/METplus_Data/v5.0

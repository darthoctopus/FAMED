import famed as f
import os
import sys
import shutil
from pathlib import Path

__all__ = ['test_steps','test_run']

def test_steps(silent_remove=False):
    # Step-by-step
    cat_id = 'KIC'
    star_id = '012069424'
    teff = 5825
    
    # Prepare clean test space
    clean_old_folder(cat_id, star_id, silent_remove=silent_remove)
    move_test_data(cat_id, star_id)

    # Run test
    star=f.Global(cat_id, star_id, teff)
    star.make_islands(force=True)
    star.find_islands(force=True)
    star.make_global_plots()

def test_run(silent_remove=False):
    # All at once
    cat_id = 'KIC'
    star_id = '006117517'
    teff = 4687
    
    # Prepare clean test space
    clean_old_folder(cat_id, star_id, silent_remove=silent_remove)
    move_test_data(cat_id, star_id)
    
    # Run test
    star = f.run.run_GLOBAL('KIC', '006117517', 4687, force=True)

def move_test_data(cat_id, star_id):
    # Copy background results and data to Background folder
    print('Copying test data over to running folders....')

    origin = Path('../../tutorials/data/Background/data')/(cat_id+star_id+'.txt')
    target_dir = Path('../../../Background/data')
    target = target_dir/(cat_id+star_id+'.txt')
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    shutil.copy(origin, target)

    origin = Path('../../tutorials/data/Background/results')/(cat_id+star_id)
    target_dir = Path('../../../Background/results')
    target = target_dir/(cat_id+star_id)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    shutil.copytree(origin, target)
    
def clean_old_folder(cat_id, star_id, silent_remove=False):
    # Remove the existing folders in PeakBagging and Background,
    # Ask for user confirmation if silent_remove is False
    print('Cleaning up existing data for a clean test....')
    
    target_bg_data = Path('../../../Background/data')/(cat_id+star_id+'.txt')
    target_pb_data = Path('../../../PeakBagging/data')/(cat_id+star_id+'.txt')
    target_bg_results = Path('../../../Background/results')/(cat_id+star_id)
    target_pb_results = Path('../../../PeakBagging/results')/(cat_id+star_id)

    if not silent_remove:
        print('\n\nFiles to be cleaned up:\n')
        print(target_bg_data.resolve(),target_pb_data.resolve(),target_bg_results.resolve(),target_pb_results.resolve(),sep='\n')
        val = input('\nOkay to remove these files...?   [y/n]:  ')
        if val in 'yYesYES':
            okay_to_remove = True
        else:
            print('Permission not given to clean out files. Aborting test')
            exit
            
    if silent_remove or okay_to_remove:
        if os.path.exists(target_bg_data):
            os.remove(target_bg_data)
        if os.path.exists(target_pb_data):
            os.remove(target_pb_data)
        if os.path.exists(target_bg_results):
            shutil.rmtree(target_bg_results)
        if os.path.exists(target_pb_results):
            shutil.rmtree(target_pb_results)

        
if __name__ == '__main__':
    silent_remove = False
    try:
        if sys.argv[1] == 'silent':
            silent_remove = True
    except:
        pass
    
    print('Testing in step-by-step mode')
    test_steps(silent_remove)

    print('Testing in run all at once mode.')
    test_run(silent_remove)

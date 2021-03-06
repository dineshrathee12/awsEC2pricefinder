from includes import print_help
from includes import read_yaml
from includes import REGION_NVIRGINIA
from awsEC2pricing import get_sys_argv
from awsEC2pricing import main
from includes import get_ec2_spot_price, get_ec2_spot_interruption
from includes import region_map

def test_print_help():
    assert print_help()

def test_read_yaml():
    # positive test
    filename = 'credentials.yaml'
    assert not read_yaml(filename) is None
    # negative test
    filename = 'credentialsx.yaml'
    assert read_yaml(filename) is None

def test_get_sys_argv_positive():
    # test with parameters
    success, text_only, pvcpu, pram, pos, pregion = get_sys_argv(['','-t','8','16','Linux',REGION_NVIRGINIA])
    assert success
    assert not text_only is None
    assert not pvcpu is None
    assert not pram is None
    assert not pos is None
    assert not pregion is None

def test_get_sys_argv_help():
    # test help
    success, text_only, pvcpu, pram, pos, pregion = get_sys_argv(['', '-h'])
    assert not success


def test_get_sys_argv_negative():
    # test incorrect parameter
    success, text_only, pvcpu, pram, pos, pregion = get_sys_argv(['', '-x'])
    assert not success
    # test incorrect cpu
    success, text_only, pvcpu, pram, pos, pregion = get_sys_argv(['', '-t', 'x'])
    assert not success
    # test incorrect ram
    success, text_only, pvcpu, pram, pos, pregion = get_sys_argv(['', '-t', '4', 'x'])
    assert not success
    # test incorrect os
    success, text_only, pvcpu, pram, pos, pregion = get_sys_argv(['', '-t', '4', '8', 'x'])
    assert not success
    # test incorrect region
    success, text_only, pvcpu, pram, pos, pregion = get_sys_argv(['', '-t', '4', '8', 'Linux', 'x'])
    assert not success


def test_spot_prices():
    instances = ['t3.medium', 't2.medium', 't3.large', 'm6g.large']
    spot_prices = get_ec2_spot_price(instances=instances, os='Linux', region=REGION_NVIRGINIA)
    assert len(spot_prices) == 4


def test_spot_interruption():
    instances = ['t3.medium', 't2.medium', 't3.large', 'm6g.large']
    spot_interrupt_rates = get_ec2_spot_interruption(instances=instances, os='Linux', region=region_map[REGION_NVIRGINIA])
    assert len(spot_interrupt_rates) == 4

def test_main():
    assert main(testing=True)
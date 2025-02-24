#!/usr/bin/env python3

import pytest

import pprint
from csv import reader

from metplus.util.string_manip import *
from metplus.util.string_manip import _fix_list


@pytest.mark.parametrize(
    'subset_definition, expected_result', [
        ([1, 3, 5], ['b', 'd', 'f']),
        ([1, 3, 5, '+'], ['b', 'd', 'f', 'g', 'h', 'i', 'j']),
        ([1], ['b']),
        (1, ['b']),
        ([3, '+'], ['d', 'e', 'f', 'g', 'h', 'i', 'j']),
        (None, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']),
        (slice(1,4,1), ['b', 'c', 'd']),
        (slice(2,9,2), ['c', 'e', 'g', 'i']),
    ]
)
@pytest.mark.util
def test_subset_list(subset_definition, expected_result):
    full_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    result = subset_list(full_list, subset_definition)
    assert result == expected_result


@pytest.mark.parametrize(
    'int_string, expected_result', [
        ('4', [4]),
        ('4-12', [4, 5, 6, 7, 8, 9, 10, 11, 12]),
        ('5,18-24,29', [5, 18, 19, 20, 21, 22, 23, 24, 29]),
        ('7,8,9,13', [7, 8, 9, 13]),
        ('4+', [4, '+']),
        ('4-12+', [4, 5, 6, 7, 8, 9, 10, 11, 12, '+']),
        ('5,18-24,29+', [5, 18, 19, 20, 21, 22, 23, 24, 29, '+']),
        ('7,8,9,13+', [7, 8, 9, 13, '+']),
    ]
)
@pytest.mark.util
def test_expand_int_string_to_list(int_string, expected_result):
    result = expand_int_string_to_list(int_string)
    assert result == expected_result


@pytest.mark.parametrize(
    'value, expected_result', [
        (3.3, 3.5),
        (3.1, 3.0),
        (-3.2, -3.0),
        (-3.8, -4.0),
    ]
)
@pytest.mark.util
def test_round_0p5(value, expected_result):
    assert round_0p5(value) == expected_result


@pytest.mark.parametrize(
    'key, value', [
        ({"gt2.3", "gt5.5"}, True),
        ({"ge2.3", "ge5.5"}, True),
        ({"eq2.3"}, True),
        ({"ne2.3"}, True),
        ({"lt2.3", "lt1.1"}, True),
        ({"le2.3", "le1.1"}, True),
        ({">2.3", ">5.5"}, True),
        ({">=2.3", ">=5.5"}, True),
        ({"==2.3"}, True),
        ({"!=.3"}, True),
        ({"<2.3", "<1."}, True),
        ({"<=2.3", "<=1.1"}, True),
        ({"gta"}, False),
        ({"gt"}, False),
        ({">=a"}, False),
        ({"2.3"}, False),
        ({"<=2.3", "2.4", "gt2.7"}, False),
        ({"<=2.3||>=4.2", "gt2.3&&lt4.2"}, True),
        ({"gt2.3&&lt4.2a"}, True),
        ({"gt2sd.3&&lt4.2"}, True),
        ({"gt2.3&a&lt4.2"}, True), # invalid but is accepted
        ({'gt4&&lt5&&ne4.5'}, True),
        ({"<2.3", "ge5", ">SPF90"}, True),
        (["NA"], True),
        (["<USP90(2.5)"], True),
        ([""], False),
        ([">SFP70", ">SFP80", ">SFP90", ">SFP95"], True),
        ([">SFP70", ">SFP80", ">SFP90", ">SFP95"], True),
    ]
)
@pytest.mark.util
def test_threshold(key, value):
    assert validate_thresholds(key) == value


# parses a threshold and returns a list of tuples of
# comparison and number, i.e.:
# 'gt4' => [('gt', 4)]
# gt4&&lt5 => [('gt', 4), ('lt', 5)]
@pytest.mark.parametrize(
    'key, value', [
        ('gt4', [('gt', 4)]),
        ('gt4&&lt5', [('gt', 4), ('lt', 5)]),
        ('gt4&&lt5&&ne4.5', [('gt', 4), ('lt', 5), ('ne', 4.5)]),
        (">4.545", [('>', 4.545)]),
        (">=4.0", [('>=', 4.0)]),
        ("<4.5", [('<', 4.5)]),
        ("<=4.5", [('<=', 4.5)]),
        ("!=4.5", [('!=', 4.5)]),
        ("==4.5", [('==', 4.5)]),
        ("gt4.5", [('gt', 4.5)]),
        ("ge4.5", [('ge', 4.5)]),
        ("lt4.5", [('lt', 4.5)]),
        ("le4.5", [('le', 4.5)]),
        ("ne10.5", [('ne', 10.5)]),
        ("eq4.5", [('eq', 4.5)]),
        ("eq-4.5", [('eq', -4.5)]),
        ("eq+4.5", [('eq', 4.5)]),
        ("eq.5", [('eq', 0.5)]),
        ("eq5.", [('eq', 5)]),
        ("eq5.||ne0.0", [('eq', 5), ('ne', 0.0)]),
        (">SFP90", [('>', 'SFP90')]),
        ("SFP90", None),
        ("gtSFP90", [('gt', 'SFP90')]),
        ("goSFP90", None),
        ("NA", [('NA', '')]),
        ("<USP90(2.5)", [('<', 'USP90(2.5)')]),
        ('gt4 && lt5', [('gt', 4), ('lt', 5)]),
        (' gt4', [('gt', 4)]),
    ]
)
@pytest.mark.util
def test_get_threshold_via_regex(key, value):
    assert get_threshold_via_regex(key) == value


@pytest.mark.parametrize(
    'camel, underscore', [
        ('ASCII2NCWrapper', 'ascii2nc_wrapper'),
        ('CyclonePlotterWrapper', 'cyclone_plotter_wrapper'),
        ('EnsembleStatWrapper', 'ensemble_stat_wrapper'),
        ('ExampleWrapper', 'example_wrapper'),
        ('ExtractTilesWrapper', 'extract_tiles_wrapper'),
        ('GempakToCFWrapper', 'gempak_to_cf_wrapper'),
        ('GenVxMaskWrapper', 'gen_vx_mask_wrapper'),
        ('GridStatWrapper', 'grid_stat_wrapper'),
        ('MODEWrapper', 'mode_wrapper'),
        ('MTDWrapper', 'mtd_wrapper'),
        ('PB2NCWrapper', 'pb2nc_wrapper'),
        ('PCPCombineWrapper', 'pcp_combine_wrapper'),
        ('Point2GridWrapper', 'point2grid_wrapper'),
        ('PointStatWrapper', 'point_stat_wrapper'),
        ('PyEmbedWrapper', 'py_embed_wrapper'),
        ('RegridDataPlaneWrapper', 'regrid_data_plane_wrapper'),
        ('SeriesAnalysisWrapper', 'series_analysis_wrapper'),
        ('StatAnalysisWrapper', 'stat_analysis_wrapper'),
        ('TCMPRPlotterWrapper', 'tcmpr_plotter_wrapper'),
        ('TCPairsWrapper', 'tc_pairs_wrapper'),
        ('TCStatWrapper', 'tc_stat_wrapper'),
    ]
)
@pytest.mark.util
def test_camel_to_underscore(camel, underscore):
    assert camel_to_underscore(camel) == underscore


@pytest.mark.parametrize(
    'before, after', [
        ('string', 'string'),
        ('"string"', 'string'),
        ('', ''),
        ('""', ''),
        (None, ''),
    ]
)
@pytest.mark.util
def test_remove_quotes(before, after):
    assert remove_quotes(before) == after


@pytest.mark.parametrize(
    'string_list, output_list', [
        # 0: list of strings
        ('gt2.7, >3.6, eq42',
         ['gt2.7', '>3.6', 'eq42']),
        # 1: one string has commas within quotes
        ('gt2.7, >3.6, eq42, "has,commas,in,it"',
         ['gt2.7', '>3.6', 'eq42', 'has,commas,in,it']),
        # 2: one string has commas and spaces within quotes
        ('gt2.7, >3.6, eq42, "has some,commas,in,it"',
         ['gt2.7', '>3.6', 'eq42', 'has some,commas,in,it']),
        # 3: empty string
        ('',
         []),
        # 4: string with commas between ()s
        ('name="CLM_NAME"; level="(0,0,*,*)"',
         ['name="CLM_NAME"; level="(0,0,*,*)"']),
        # 5: string with commas between ()s and commas not between ()s
        ('name="CLM_NAME"; level="(0,0,*,*)";, name="OTHER"; level="A06"',
         ['name="CLM_NAME"; level="(0,0,*,*)";', 'name="OTHER"; level="A06"']),
        # 6: string with commas between ()s within {}s
        ('{name="CLM_NAME"; level="(0,0,*,*)";}',
         ['{name="CLM_NAME"; level="(0,0,*,*)";}']),
        # 7: multiple {}s with string with commas between ()s
        ('{name="CLM_NAME"; level="(0,0,*,*)";},{name="CLM_NAME"; level="(0,0,*,*)";}',
         ['{name="CLM_NAME"; level="(0,0,*,*)";}',
          '{name="CLM_NAME"; level="(0,0,*,*)";}']),
        # 8: read example with commas beween ()s
        ('-input_field \'name="TEC"; level="({valid?fmt=%Y%m%d_%H%M%S},*,*)"; file_type=NETCDF_NCCF;\'',
         ['-input_field \'name="TEC"; level="({valid?fmt=%Y%m%d_%H%M%S},*,*)"; file_type=NETCDF_NCCF;\'']),
        # 9: read example commas separating quotes within []s
        ('{name="UGRD"; level=["P850","P500","P250"];}',
         ['{name="UGRD"; level=["P850","P500","P250"];}']),
        # 10: multiples {}s with commas separating quotes within []s
        ('{name="UGRD"; level=["P850","P500","P250"];}, {name="UGRD"; level=["P750","P600"];}',
         ['{name="UGRD"; level=["P850","P500","P250"];}', '{name="UGRD"; level=["P750","P600"];}']),
        # 11: list with square braces and ending semi-colon (MET format)
        ('["{ENV[MET_BUILD_BASE]}/share/met/poly/CAR.poly", "{ENV[MET_BUILD_BASE]}/share/met/poly/GLF.poly"];',
         ["{ENV[MET_BUILD_BASE]}/share/met/poly/CAR.poly", "{ENV[MET_BUILD_BASE]}/share/met/poly/GLF.poly"]),
        # 12: list with square braces and ending semi-colon (MET format) no quotes
        ('[MET_BASE/poly/LMV.poly];',
         ["MET_BASE/poly/LMV.poly"]),
        # 13: single item ending with semi-colon should keep semi-colon
        ('file_type = NETCDF_NCCF;',
         ["file_type = NETCDF_NCCF;"]),
        # 14: list with line break at beginning
        ('\nsome_value,\n some_other_value',
         ["some_value", "some_other_value"]),
    ]
)
@pytest.mark.util
def test_getlist(string_list, output_list):
    test_list = getlist(string_list)
    assert test_list == output_list


@pytest.mark.util
def test_getlist_int():
    string_list = '6, 7, 42'
    test_list = getlistint(string_list)
    assert test_list == [6, 7, 42]


@pytest.mark.parametrize(
    'list_string, output_list', [
        ('begin_end_incr(3,12,3)',
         ['3', '6', '9', '12']),

        ('1,2,3,4',
         ['1', '2', '3', '4']),

        (' 1,2,3,4',
         ['1', '2', '3', '4']),

        ('1,2,3,4 ',
         ['1', '2', '3', '4']),

        (' 1,2,3,4 ',
         ['1', '2', '3', '4']),

        ('1, 2,3,4',
         ['1', '2', '3', '4']),

        ('1,2, 3, 4',
         ['1', '2', '3', '4']),

        ('begin_end_incr( 3,12 , 3)',
         ['3', '6', '9', '12']),

        ('begin_end_incr(0,10,2)',
         ['0', '2', '4', '6', '8', '10']),

        ('begin_end_incr(10,0,-2)',
         ['10', '8', '6', '4', '2', '0']),

        ('begin_end_incr(2,2,20)',
         ['2']),

        ('begin_end_incr(0,2,1), begin_end_incr(3,9,3)',
         ['0', '1', '2', '3', '6', '9']),

        ('mem_begin_end_incr(0,2,1), mem_begin_end_incr(3,9,3)',
         ['mem_0', 'mem_1', 'mem_2', 'mem_3', 'mem_6', 'mem_9']),

        ('mem_begin_end_incr(0,2,1,3), mem_begin_end_incr(3,12,3,3)',
         ['mem_000', 'mem_001', 'mem_002', 'mem_003',
          'mem_006', 'mem_009', 'mem_012']),

        ('begin_end_incr(0,10,2)H, 12',
         ['0H', '2H', '4H', '6H', '8H', '10H', '12']),

        ('begin_end_incr(0,10800,3600)S, 4H',
         ['0S', '3600S', '7200S', '10800S', '4H']),

        ('data.{init?fmt=%Y%m%d%H?shift=begin_end_incr(0, 3, 3)H}.ext',
         ['data.{init?fmt=%Y%m%d%H?shift=0H}.ext',
          'data.{init?fmt=%Y%m%d%H?shift=3H}.ext',
          ]),
        ('"%m:begin_end_incr(3,11,1)", "%m%d:0229"',
         ['%m:3', '%m:4', '%m:5', '%m:6', '%m:7', '%m:8', '%m:9', '%m:10',
          '%m:11', '%m%d:0229'])
    ]
)
@pytest.mark.util
def test_getlist_begin_end_incr(list_string, output_list):
    assert getlist(list_string) == output_list


@pytest.mark.parametrize(
    'input, add_quotes, expected_output', [
        (['a', 'b', 'c'], None, '"a", "b", "c"'),
        (['0', '1', '2'], None, '"0", "1", "2"'),
        (['a', 'b', 'c'], True, '"a", "b", "c"'),
        (['0', '1', '2'], True, '"0", "1", "2"'),
        (['a', 'b', 'c'], False, 'a, b, c'),
        (['0', '1', '2'], False, '0, 1, 2'),
        (['"a"', '"b"', '"c"'], True, '"a", "b", "c"'),
        (['"0"', '"1"', '"2"'], True, '"0", "1", "2"'),
    ]
)
@pytest.mark.util
def test_list_to_str(input, add_quotes, expected_output):
    if add_quotes is None:
        assert list_to_str(input) == expected_output
    else:
        assert list_to_str(input, add_quotes=add_quotes) == expected_output


@pytest.mark.parametrize(
    'expression, expected_result', [
        ('gt3', 'gt3'),
        ('>3', 'gt3'),
        ('le3.5', 'le3.5'),
        ('<=3.5', 'le3.5'),
        ('==4', 'eq4'),
        ('!=3.5', 'ne3.5'),
    ]
)
@pytest.mark.util
def test_comparison_to_letter_format(expression, expected_result):
    assert comparison_to_letter_format(expression) == expected_result


@pytest.mark.parametrize(
    'expression, expected_result', [
        ('>1', 'gt1'),
        ('>=0.2', 'ge0.2'),
        ('<30', 'lt30'),
        ('<=0.04', 'le0.04'),
        ('==5', 'eq5'),
        ('!=0.06', 'ne0.06'),
        ('>0.05, gt0.05, >=1, ge1, <5, lt5, <=10, le10, ==15, eq15, !=20, ne20',
         'gt0.05,gt0.05,ge1,ge1,lt5,lt5,le10,le10,eq15,eq15,ne20,ne20'),
        ('<805, <1609, <4828, <8045, >=8045, <16090',
         'lt805,lt1609,lt4828,lt8045,ge8045,lt16090'),
    ]
)
@pytest.mark.util
def test_format_thresh(expression, expected_result):
    assert format_thresh(expression) == expected_result


@pytest.mark.parametrize(
    'level, expected_result', [
        ('level', 'level'),
        ('P500', 'P500'),
        ('*,*', 'all_all'),
        ('1,*,*', '1_all_all'),
    ]
)
@pytest.mark.util
def test_format_level(level, expected_result):
    assert format_level(level) == expected_result


@pytest.mark.parametrize(
    'regex,index,id,expected_result', [
        # 0: No ID
        (r'^FCST_VAR(\d+)_NAME$', 1, None,
         {'1': [None],
          '2': [None],
          '4': [None]}),
        # 1: ID and index 2
        (r'(\w+)_VAR(\d+)_NAME', 2, 1,
         {'1': ['FCST'],
          '2': ['FCST'],
          '4': ['FCST']}),
        # 2: index 1, ID 2, multiple identifiers
        (r'^FCST_VAR(\d+)_(\w+)$', 1, 2,
         {'1': ['NAME', 'LEVELS'],
          '2': ['NAME'],
          '4': ['NAME']}),
        # 3: command that StatAnalysis wrapper uses
        (r'MODEL(\d+)$', 1, None,
         {'1': [None],
          '2': [None],}),
        # 4: TCPairs conensus logic
        (r'^TC_PAIRS_CONSENSUS(\d+)_(\w+)$', 1, 2,
         {'1': ['NAME', 'MEMBERS', 'REQUIRED', 'MIN_REQ'],
          '2': ['NAME', 'MEMBERS', 'REQUIRED', 'MIN_REQ']}),
    ]
)
@pytest.mark.util
def test_find_indices_in_config_section(metplus_config, regex, index,
                                        id, expected_result):
    config = metplus_config
    config.set('config', 'FCST_VAR1_NAME', 'name1')
    config.set('config', 'FCST_VAR1_LEVELS', 'level1')
    config.set('config', 'FCST_VAR2_NAME', 'name2')
    config.set('config', 'FCST_VAR4_NAME', 'name4')
    config.set('config', 'MODEL1', 'model1')
    config.set('config', 'MODEL2', 'model2')

    config.set('config', 'TC_PAIRS_CONSENSUS1_NAME', 'name1')
    config.set('config', 'TC_PAIRS_CONSENSUS1_MEMBERS', 'member1')
    config.set('config', 'TC_PAIRS_CONSENSUS1_REQUIRED', 'True')
    config.set('config', 'TC_PAIRS_CONSENSUS1_MIN_REQ', '1')
    config.set('config', 'TC_PAIRS_CONSENSUS2_NAME', 'name2')
    config.set('config', 'TC_PAIRS_CONSENSUS2_MEMBERS', 'member2')
    config.set('config', 'TC_PAIRS_CONSENSUS2_REQUIRED', 'True')
    config.set('config', 'TC_PAIRS_CONSENSUS2_MIN_REQ', '2')

    indices = find_indices_in_config_section(regex, config, index_index=index,
                                             id_index=id)

    pp = pprint.PrettyPrinter()
    print(f'Indices:')
    pp.pprint(indices)

    assert indices == expected_result

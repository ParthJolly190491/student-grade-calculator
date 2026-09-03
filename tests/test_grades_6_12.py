# tests/test_grades_6_12.py — Student Grade Calculator Tests

import pytest
from grades_6_12 import (
    calculate_letter_grade,
    calculate_average,
    calculate_gpa,
    get_student_summary,
    is_passing,
    get_passing_percentage,
    count_failing,
    get_grade_distribution,
    find_top_score,
    find_lowest_score,
    calculate_score_range,
)


# ── calculate_letter_grade ─────────────────────────────────────────────────

def test_calculate_letter_grade_A():
    assert calculate_letter_grade(95) == "A"

def test_calculate_letter_grade_B():
    assert calculate_letter_grade(85) == "B"

def test_calculate_letter_grade_F():
    assert calculate_letter_grade(50) == "F"

def test_calculate_letter_grade_boundary_exactly_90():
    assert calculate_letter_grade(90) == "A"

def test_calculate_letter_grade_invalid_above_100():
    with pytest.raises(ValueError):
        calculate_letter_grade(110)

def test_calculate_letter_grade_invalid_negative():
    with pytest.raises(ValueError):
        calculate_letter_grade(-5)


# ── calculate_average ──────────────────────────────────────────────────────

def test_calculate_average_returns_correct_value():
    assert calculate_average([80, 90, 70]) == 80.0

def test_calculate_average_single_score():
    assert calculate_average([100]) == 100.0

def test_calculate_average_empty_list_raises():
    with pytest.raises(ValueError):
        calculate_average([])


# ── calculate_gpa ──────────────────────────────────────────────────────────

def test_calculate_gpa_all_A():
    assert calculate_gpa(["A", "A", "A"]) == 4.0

def test_calculate_gpa_mixed_grades():
    assert calculate_gpa(["A", "B", "C"]) == 3.0

def test_calculate_gpa_empty_list_raises():
    with pytest.raises(ValueError):
        calculate_gpa([])

def test_calculate_gpa_invalid_grade_raises():
    with pytest.raises(ValueError):
        calculate_gpa(["A", "X", "B"])


# ── get_student_summary ────────────────────────────────────────────────────

def test_get_student_summary_contains_name():
    result = get_student_summary("Alice", [90, 85, 92])
    assert "Alice" in result

def test_get_student_summary_blank_name_raises():
    with pytest.raises(ValueError):
        get_student_summary("  ", [90, 85])

def test_get_student_summary_empty_scores_raises():
    with pytest.raises(ValueError):
        get_student_summary("Bob", [])


# ── is_passing ──────────────────────────────────────────────────────────────

def test_is_passing_returns_true_for_passing_score():
    assert is_passing(75) is True

def test_is_passing_returns_false_for_failing_score():
    assert is_passing(50) is False

def test_is_passing_boundary_exactly_60():
    assert is_passing(60) is True

def test_is_passing_invalid_negative():
    with pytest.raises(ValueError):
        is_passing(-5)

def test_is_passing_invalid_above_100():
    with pytest.raises(ValueError):
        is_passing(110)


# ── get_passing_percentage ──────────────────────────────────────────────────

def test_get_passing_percentage_all_passing():
    assert get_passing_percentage([80, 90, 70]) == 100.0

def test_get_passing_percentage_all_failing():
    assert get_passing_percentage([50, 40, 30]) == 0.0

def test_get_passing_percentage_mixed():
    assert get_passing_percentage([80, 50, 70, 55]) == 50.0

def test_get_passing_percentage_single_passing():
    assert get_passing_percentage([75]) == 100.0

def test_get_passing_percentage_empty_list_raises():
    with pytest.raises(ValueError):
        get_passing_percentage([])


# ── count_failing ───────────────────────────────────────────────────────────

def test_count_failing_all_failing():
    assert count_failing([50, 40, 30]) == 3

def test_count_failing_all_passing():
    assert count_failing([80, 90, 70]) == 0

def test_count_failing_mixed():
    assert count_failing([80, 50, 70, 55]) == 2

def test_count_failing_single_failing():
    assert count_failing([45]) == 1

def test_count_failing_empty_list_raises():
    with pytest.raises(ValueError):
        count_failing([])


# ── get_grade_distribution ────────────────────────────────────────────────

def test_get_grade_distribution_returns_all_grades():
    result = get_grade_distribution([95, 85, 75, 65, 55])
    assert result == {"A": 1, "B": 1, "C": 1, "D": 1, "F": 1}

def test_get_grade_distribution_all_same_grade():
    result = get_grade_distribution([95, 92, 91])
    assert result == {"A": 3, "B": 0, "C": 0, "D": 0, "F": 0}

def test_get_grade_distribution_empty_list_raises():
    with pytest.raises(ValueError):
        get_grade_distribution([])


# ── find_top_score ─────────────────────────────────────────────────────────

def test_find_top_score_returns_highest():
    assert find_top_score([75, 92, 88, 95]) == 95.0

def test_find_top_score_single_score():
    assert find_top_score([85]) == 85.0

def test_find_top_score_empty_list_raises():
    with pytest.raises(ValueError):
        find_top_score([])


# ── find_lowest_score ────────────────────────────────────────────────────────

def test_find_lowest_score_returns_lowest():
    assert find_lowest_score([75, 92, 88, 95]) == 75.0

def test_find_lowest_score_single_score():
    assert find_lowest_score([85]) == 85.0

def test_find_lowest_score_empty_list_raises():
    with pytest.raises(ValueError):
        find_lowest_score([])


# ── calculate_score_range ─────────────────────────────────────────────────

def test_calculate_score_range_returns_difference():
    assert calculate_score_range([75, 92, 88, 95]) == 20.0

def test_calculate_score_range_single_score():
    assert calculate_score_range([85]) == 0.0

def test_calculate_score_range_empty_list_raises():
    with pytest.raises(ValueError):
        calculate_score_range([])

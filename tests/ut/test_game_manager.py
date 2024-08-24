import sys
from typing import Iterator
from unittest.mock import patch

import pytest

from game_manager import GameManager, GameStates


@pytest.fixture
def game_manager() -> Iterator[GameManager]:
    yield GameManager()


def test_game_manager_start_sets_state_to_on_going(game_manager: GameManager) -> None:
    game_manager.start()

    assert game_manager.state == GameStates.OnGoing


def test_game_manager_pause_sets_state_to_paused(game_manager: GameManager) -> None:
    game_manager.pause()

    assert game_manager.state == GameStates.Paused


def test_game_manager_exit_calls_sys_exit_with_0(game_manager: GameManager) -> None:
    with patch.object(sys, "exit") as sys_exit_spy:
        game_manager.exit()

    sys_exit_spy.assert_called_once_with(0)

import pytest
from unittest.mock import Mock, MagicMock

from app.modules.notepad.services import NotepadService
from app.modules.notepad.repositories import NotepadRepository


class TestNotepadService:
    
    
    @pytest.fixture
    def service_and_mock_repository(self):
        """Fixture to provide a service with mocked repository"""
        mock_repository = Mock(spec=NotepadRepository)
        service = NotepadService()
        service.repository = mock_repository
        return service, mock_repository

    def test_get_all_by_user_calls_repository_method(self, service_and_mock_repository):
        """Test that get_all_by_user correctly calls the repository method"""
        service, mock_repository = service_and_mock_repository
        mock_repository.get_all_by_user.return_value = []

        user_id = 123
        
        result = service.get_all_by_user(user_id)
        
        mock_repository.get_all_by_user.assert_called_once_with(user_id)
        assert result == []

    def test_get_all_by_user_returns_repository_result(self, service_and_mock_repository):
        """Test that get_all_by_user returns exactly what the repository returns"""
        service, mock_repository = service_and_mock_repository
        expected_notepads = [
            Mock(id=1, title="Note 1", user_id=123),
            Mock(id=2, title="Note 2", user_id=123)
        ]
        mock_repository.get_all_by_user.return_value = expected_notepads
        
        user_id = 123

        result = service.get_all_by_user(user_id)

        assert result == expected_notepads
        mock_repository.get_all_by_user.assert_called_once_with(user_id)
import pytest_mock as ptm

from ghsa.__main__ import upload_secret


def test_upload_secret(mocker: ptm.MockFixture) -> None:
    put = mocker.patch('requests.put')

    upload_secret(
        mocker.ANY,
        mocker.ANY,
        mocker.ANY,
        mocker.ANY,
        mocker.ANY,
    )

    put.assert_called_once_with(
        mocker.ANY,
        headers=mocker.ANY,
        json=mocker.ANY,
    )

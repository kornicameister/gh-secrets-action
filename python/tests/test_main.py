import pytest_mock as ptm

from ghsa.__main__ import main


def test_no_secrets(mocker: ptm.MockFixture) -> None:
    get_encryption_key, encrypt_using_key, upload_secret, sys_exit = (
        mocker.patch('ghsa.__main__.get_encryption_key'),
        mocker.patch('ghsa.__main__.encrypt_using_key'),
        mocker.patch('ghsa.__main__.upload_secret'),
        mocker.patch('sys.exit'),
    )

    main({}, mocker.ANY, mocker.ANY)

    assert not get_encryption_key.called
    assert not encrypt_using_key.called
    assert not upload_secret.called
    sys_exit.assert_called_once_with(0)


def test_secrets(mocker: ptm.MockFixture) -> None:
    get_encryption_key, encrypt_using_key, upload_secret, sys_exit = (
        mocker.patch('ghsa.__main__.get_encryption_key'),
        mocker.patch('ghsa.__main__.encrypt_using_key'),
        mocker.patch('ghsa.__main__.upload_secret'),
        mocker.patch('sys.exit'),
    )

    encryption_key = mocker.Mock(spec=str)
    encryption_key_id = mocker.Mock(spec=str)
    get_encryption_key.return_value = encryption_key, encryption_key_id

    encrypt_using_key.return_value = mocker.ANY

    main(
        {
            'a': '1',
            'b': '2',
        },
        'repo',
        'token',
    )

    get_encryption_key.assert_called_once_with('repo', 'token')

    assert encrypt_using_key.call_count == 2
    encrypt_using_key.assert_any_call('1', key=encryption_key)
    encrypt_using_key.assert_any_call('2', key=encryption_key)

    assert upload_secret.call_count == 2
    upload_secret.assert_any_call('repo', 'token', encryption_key_id, 'a', mocker.ANY)
    upload_secret.assert_any_call('repo', 'token', encryption_key_id, 'b', mocker.ANY)

    assert not sys_exit.called

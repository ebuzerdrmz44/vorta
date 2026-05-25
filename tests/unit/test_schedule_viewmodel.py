from vorta.store.models import BackupProfileModel
from vorta.views.viewmodels.schedule_page_viewmodel import SchedulePageViewModel


def test_get_schedule_data():
    """Test that the ViewModel reads all schedule attributes from the profile."""
    viewmodel = SchedulePageViewModel()
    profile = BackupProfileModel.get(id=1)

    profile.schedule_mode = 'interval'
    profile.schedule_interval_unit = 'hours'
    profile.schedule_interval_count = 3
    profile.schedule_fixed_hour = 14
    profile.schedule_fixed_minute = 30
    profile.save()

    data = viewmodel.get_schedule_data(profile)

    assert data['schedule_mode'] == 'interval'
    assert data['schedule_interval_unit'] == 'hours'
    assert data['schedule_interval_count'] == 3
    assert data['schedule_fixed_hour'] == 14
    assert data['schedule_fixed_minute'] == 30


def test_save_schedule():
    """Test that the ViewModel saves schedule fields to the database."""
    viewmodel = SchedulePageViewModel()
    profile = BackupProfileModel.get(id=1)

    viewmodel.save_schedule(profile, 'fixed', 'days', 1, 8, 15)

    updated = BackupProfileModel.get(id=1)
    assert updated.schedule_mode == 'fixed'
    assert updated.schedule_interval_unit == 'days'
    assert updated.schedule_interval_count == 1
    assert updated.schedule_fixed_hour == 8
    assert updated.schedule_fixed_minute == 15


def test_save_schedule_preserves_other_fields():
    """Test that saving schedule data does not overwrite unrelated profile fields."""
    viewmodel = SchedulePageViewModel()
    profile = BackupProfileModel.get(id=1)

    profile.compression = 'lz4'
    profile.prune_on = True
    profile.save()

    viewmodel.save_schedule(profile, 'interval', 'hours', 6, 0, 0)

    updated = BackupProfileModel.get(id=1)
    assert updated.compression == 'lz4'
    assert updated.prune_on is True

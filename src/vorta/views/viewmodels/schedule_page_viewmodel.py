class SchedulePageViewModel:
    def get_schedule_data(self, profile):
        """Reads the schedule data from DB"""
        return {
            'schedule_mode': profile.schedule_mode,
            'schedule_interval_unit': profile.schedule_interval_unit,
            'schedule_interval_count': profile.schedule_interval_count,
            'schedule_fixed_hour': profile.schedule_fixed_hour,
            'schedule_fixed_minute': profile.schedule_fixed_minute,
            'validation_on': profile.validation_on,
            'validation_weeks': profile.validation_weeks,
            'compaction_on': profile.compaction_on,
            'compaction_weeks': profile.compaction_weeks,
            'prune_on': profile.prune_on,
            'schedule_make_up_missed': profile.schedule_make_up_missed,
        }

    def save_schedule(self, profile, schedule_mode, interval_unit,
                      interval_count, fixed_hour, fixed_minute):
        """Writes the changed schedule data"""
        profile.schedule_mode = schedule_mode
        profile.schedule_interval_unit = interval_unit
        profile.schedule_interval_count = interval_count
        profile.schedule_fixed_hour = fixed_hour
        profile.schedule_fixed_minute = fixed_minute
        profile.save()

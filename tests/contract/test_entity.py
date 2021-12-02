# -*- coding: utf-8 -*-
from zvt.contract import TradableEntity, IntervalLevel
from zvt.utils.time_utils import to_pd_timestamp


def test_get_1min_timestamps():
    timestamps = [
        timestamp
        for timestamp in TradableEntity.get_interval_timestamps(
            start_date='2020-06-17',
            end_date='2020-06-18',
            level=IntervalLevel.LEVEL_1MIN,
        )
    ]

    assert to_pd_timestamp('2020-06-17 09:31:00') in timestamps
    assert to_pd_timestamp('2020-06-17 11:30:00') in timestamps
    assert to_pd_timestamp('2020-06-17 13:01:00') in timestamps
    assert to_pd_timestamp('2020-06-17 15:00:00') in timestamps

    assert to_pd_timestamp('2020-06-17 09:31:00') in timestamps
    assert to_pd_timestamp('2020-06-17 11:30:00') in timestamps
    assert to_pd_timestamp('2020-06-17 13:01:00') in timestamps
    assert to_pd_timestamp('2020-06-18 15:00:00') in timestamps


def test_get_1h_timestamps():
    timestamps = [
        timestamp
        for timestamp in TradableEntity.get_interval_timestamps(
            start_date='2020-06-17',
            end_date='2020-06-18',
            level=IntervalLevel.LEVEL_1HOUR,
        )
    ]

    assert to_pd_timestamp('2020-06-17 10:30:00') in timestamps
    assert to_pd_timestamp('2020-06-17 11:30:00') in timestamps
    assert to_pd_timestamp('2020-06-17 14:00:00') in timestamps
    assert to_pd_timestamp('2020-06-17 15:00:00') in timestamps

    assert to_pd_timestamp('2020-06-17 10:30:00') in timestamps
    assert to_pd_timestamp('2020-06-17 11:30:00') in timestamps
    assert to_pd_timestamp('2020-06-17 14:00:00') in timestamps
    assert to_pd_timestamp('2020-06-18 15:00:00') in timestamps


def test_is_finished_kdata_timestamp():
    assert TradableEntity.is_finished_kdata_timestamp('2020-06-17 10:30', IntervalLevel.LEVEL_30MIN)
    assert not TradableEntity.is_finished_kdata_timestamp('2020-06-17 10:30', IntervalLevel.LEVEL_1DAY)

    assert TradableEntity.is_finished_kdata_timestamp('2020-06-17 11:30', IntervalLevel.LEVEL_30MIN)
    assert not TradableEntity.is_finished_kdata_timestamp('2020-06-17 11:30', IntervalLevel.LEVEL_1DAY)

    assert TradableEntity.is_finished_kdata_timestamp('2020-06-17 13:30', IntervalLevel.LEVEL_30MIN)
    assert not TradableEntity.is_finished_kdata_timestamp('2020-06-17 13:30', IntervalLevel.LEVEL_1DAY)


def test_open_close():
    assert TradableEntity.is_open_timestamp('2020-06-17 09:30')
    assert TradableEntity.is_close_timestamp('2020-06-17 15:00')

    timestamps = [
        timestamp
        for timestamp in TradableEntity.get_interval_timestamps(
            start_date='2020-06-17',
            end_date='2020-06-18',
            level=IntervalLevel.LEVEL_1HOUR,
        )
    ]

    assert TradableEntity.is_open_timestamp(timestamps[0])
    assert TradableEntity.is_close_timestamp(timestamps[-1])

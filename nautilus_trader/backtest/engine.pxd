# -------------------------------------------------------------------------------------------------
#  Copyright (C) 2015-2021 Nautech Systems Pty Ltd. All rights reserved.
#  https://nautechsystems.io
#
#  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------------------------

from cpython.datetime cimport datetime
from cpython.datetime cimport timedelta
from libc.stdint cimport int64_t

from nautilus_trader.analysis.performance cimport PerformanceAnalyzer
from nautilus_trader.backtest.data_producer cimport DataProducerFacade
from nautilus_trader.backtest.models cimport FillModel
from nautilus_trader.common.clock cimport Clock
from nautilus_trader.common.logging cimport Logger
from nautilus_trader.common.logging cimport LoggerAdapter
from nautilus_trader.common.uuid cimport UUIDFactory
from nautilus_trader.core.uuid cimport UUID
from nautilus_trader.data.engine cimport DataEngine
from nautilus_trader.execution.engine cimport ExecutionEngine
from nautilus_trader.model.c_enums.oms_type cimport OMSType
from nautilus_trader.model.identifiers cimport Venue
from nautilus_trader.risk.engine cimport RiskEngine
from nautilus_trader.trading.portfolio cimport Portfolio
from nautilus_trader.trading.trader cimport Trader


cdef class BacktestEngine:
    cdef Clock _clock
    cdef Clock _test_clock
    cdef UUIDFactory _uuid_factory
    cdef DataEngine _data_engine
    cdef ExecutionEngine _exec_engine
    cdef RiskEngine _risk_engine
    cdef DataProducerFacade _data_producer
    cdef LoggerAdapter _log
    cdef Logger _logger
    cdef Logger _test_logger
    cdef bint _log_to_file
    cdef bint _exec_db_flush
    cdef dict _exchanges

    cdef readonly Trader trader
    cdef readonly UUID system_id
    cdef readonly datetime created_time
    cdef readonly timedelta time_to_initialize
    cdef readonly int iteration
    cdef readonly Portfolio portfolio
    cdef readonly PerformanceAnalyzer analyzer

    cpdef ExecutionEngine get_exec_engine(self)
    cpdef void add_exchange(
        self,
        Venue venue,
        OMSType oms_type,
        list starting_balances,
        bint is_frozen_account=*,
        list modules=*,
        FillModel fill_model=*,
    ) except *
    cpdef void reset(self) except *
    cpdef void dispose(self) except *
    cpdef void change_fill_model(self, Venue venue, FillModel model) except *
    cpdef void run(
        self,
        datetime start=*,
        datetime stop=*,
        list strategies=*,
    ) except *

    cdef inline void _advance_time(self, int64_t now_ns) except *
    cdef inline void _process_modules(self, int64_t now_ns) except *
    cdef inline void _log_header(
        self,
        datetime run_started,
        datetime start,
        datetime stop,
    ) except *
    cdef inline void _log_footer(
        self,
        datetime run_started,
        datetime run_finished,
        datetime start,
        datetime stop,
    ) except *

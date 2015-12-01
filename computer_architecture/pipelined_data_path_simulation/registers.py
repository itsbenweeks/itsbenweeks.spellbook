#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Benjamin Weeks
CS472 Project 3
November, 22nd, 2015
"""

OPCODES = {
    0x4: 'beq',
    0x5: 'bne',
    0x23: 'lw',
    0x2b: 'sw',
    0x20: 'lb',
    0x28: 'sb'
}

FUNCTIONS = {
    0x20: 'add',
    0x22: 'sub',
    0: 'nop'
}

# For inital testing from the packet
OPERATIONS = {
    0x20: 'add',
    0x22: 'sub',
    0x24: 'and',
    0x25: 'or'
}


class Register(object):
    """Implementation of a register with a string function."""
    def __init__(self):
        self.function = 0
        self.opcode = None

    def __str__(self):
        pass

    def _operation(self):
        if self.function is not None:
            return FUNCTIONS[self.function]
        else:
            return OPCODES[self.opcode]

    def _x_or_decimal(self, var):
        if var is None:
            return 'X'
        else:
            return "{:d}".format(var)

    def _x_or_hex(self, var):
        if var is None:
            return 'X'
        else:
            return "{}".format(hex(var))

    def _x_or_string(self, var):
        if var is None:
            return 'X'
        else:
            return var


class IFIDRegister(Register):
    """Implementation of 64-bit register with a string function.
    IF/ID_Read (read by the ID stage)
    Inst = 0x10c8fffb [ beq $6, $8, label ] IncrPC = 7A014
    """
    def __init__(self):
        self.nop = True
        self.inst = None
        self.incr_pc = 0
        self.mips_inst = ""
        self.function = 0
        self.opcode = None

    def __str__(self):
        if self.function == 0:
            result = "Inst = {0:#010x}".format(0)
        else:
            result = """Inst = {0:#010x}   [ {1} ]   IncrPC = {2:05X}
                """.format(self.inst, self.mips_inst, self.incr_pc)
        return result


class IDEXRegister(Register):
    """Implementation of 128-bit register with a string function.
    ID/EX_Read (read by the EX stage)
    Control: RegDst=1, ALUSrc=0, ALUOp=10, MemRead=0, MemWrite=0,
             Branch=0, MemToReg=0, RegWrite=1, [sub]

    Incr_PC = 7A010 ReadReg1Value = 30003 ReadReg2Value = 30002
    SEOffset = X WriteReg_20_16 = 2 WriteReg_15_11 = 10 Function = 22
    """
    def __init__(self):
        self.nop = True
        self.reg_dst = False
        self.alu_src = False
        self.alu_op = 0b00
        self.mem_read = False
        self.mem_write = False
        self.branch = False
        self.mem_to_reg = None
        self.reg_write = False
        self.incr_pc = 0
        self.read_reg1_value = 0
        self.read_reg2_value = 0
        self.se_offset = None
        self.write_reg_20_16 = 0
        self.write_reg_15_11 = 0
        self.function = 0
        self.opcode = None

    def __str__(self):
        if self.function == 0:
            result = "Control = {0:#010x}".format(0)
        else:
            result = """Control: RegDst={}, ALUSrc={}, ALUOp={:b}, MemRead={}, MemWrite={},
 Branch={}, MemToReg={}, RegWrite={}, [{}]
Incr PC = {}  ReadReg1Value = {} ReadReg2Value = {}
SEOffset = {} WriteReg_20_16 = {} WriteReg_15_11 = {} Function = {}
            """.format(self._x_or_decimal(self.reg_dst),
                       self.alu_src,
                       self.alu_op,
                       self.mem_read,
                       self.mem_write,
                       self.branch,
                       self._x_or_decimal(self.mem_to_reg),
                       self.reg_write,
                       self._operation(),
                       self.incr_pc,
                       self.read_reg1_value,
                       self.read_reg2_value,
                       self._x_or_hex(self.se_offset),
                       self.write_reg_20_16,
                       self.write_reg_15_11,
                       self._x_or_hex(self.function))
        return result


class EXMEMRegister(Register):
    """Implementation of 97-bit register with a string function.
    EX/MEM_Write (written to by the EX stage)
    Control: MemRead=0, MemWrite=1, Branch=0, MemToReg=X, RegWrite=0, [sw]
    CalcBTA = X Zero = F ALUResult = 30004
    SWValue = 30009 WriteRegNum = X
    """
    def __init__(self):
        self.nop = True
        self.mem_read = False
        self.mem_write = False
        self.branch = False
        self.mem_to_reg = None
        self.reg_write = False
        self.function = 0
        self.opcode = None
        self.calc_bta = None
        self.zero = False
        self.alu_result = None
        self.sw_value = 0
        self.write_reg_num = None

    def __str__(self):
        if self.function == 0:
            result = "Control = {0:#010x}".format(0)
        else:
            # TODO: Handle Branch Target Address when None
            result = """Control: MemRead={}, MemWrite={}, Branch={}, MemToReg={}, RegWrite={}, [{}]
CalcBTA = {} Zero = {} ALUResult = {:05x}
SWValue = {:05x} WriteRegNum = {}
            """.format(self.mem_read,
                       self.mem_write,
                       self.branch,
                       self._x_or_decimal(self.mem_to_reg),
                       self.reg_write,
                       self._operation(),
                       self._x_or_hex(self.calc_bta),
                       self.zero,
                       self.alu_result,
                       self.sw_value,
                       self._x_or_decimal(self.write_reg_num))
        return result


class MEMWBRegister(Register):
    """Implementation of 64-bit register with a string function.
    MEM/WB
    Control: MemToReg=X, RegWrite=0, [sw]
    LWDataValue = X ALUResult = 30004 WriteRegNum = X

    Control: MemToReg=1, RegWrite=1, [lw]
    LWDataValue = mem contents @ 3000C ALUResult = 3000C WriteRegNum = 15"""
    def __init__(self):
        self.nop = True
        self.mem_to_reg = None
        self.reg_write = False
        self.function = 0
        self.opcode = None
        self.lw_data_value = None
        self.alu_result = None
        self.write_reg_num = None

    def __str__(self):
        if self.function == 0:
            result = "Control = {0:#010x}".format(0)
        else:
            result = """Control: MemToReg={}, RegWrite={}, [{}]
LWDataValue = {} ALUResult = {} WriteRegNum =
            """.format(self.mem_to_reg,
                       self.reg_write,
                       self._operation(),
                       self._x_or_hex(self.lw_data_value),
                       self.alu_result,
                       self.write_reg_num)
        return result

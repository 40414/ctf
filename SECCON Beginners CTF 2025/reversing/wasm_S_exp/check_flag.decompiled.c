export memory memory(initial: 1, max: 0);

export function check_flag():int {
  if (123 != f_b(38)[0]:ubyte) { return 0 }
  if (103 != f_b(20)[0]:ubyte) { return 0 }
  if (95 != f_b(46)[0]:ubyte) { return 0 }
  if (33 != f_b(3)[0]:ubyte) { return 0 }
  if (99 != f_b(18)[0]:ubyte) { return 0 }
  if (110 != f_b(119)[0]:ubyte) { return 0 }
  if (95 != f_b(51)[0]:ubyte) { return 0 }
  if (121 != f_b(59)[0]:ubyte) { return 0 }
  if (52 != f_b(9)[0]:ubyte) { return 0 }
  if (87 != f_b(4)[0]:ubyte) { return 0 }
  if (53 != f_b(37)[0]:ubyte) { return 0 }
  if (51 != f_b(12)[0]:ubyte) { return 0 }
  if (98 != f_b(111)[0]:ubyte) { return 0 }
  if (99 != f_b(45)[0]:ubyte) { return 0 }
  if (125 != f_b(97)[0]:ubyte) { return 0 }
  if (48 != f_b(54)[0]:ubyte) { return 0 }
  if (116 != f_b(112)[0]:ubyte) { return 0 }
  if (49 != f_b(106)[0]:ubyte) { return 0 }
  if (102 != f_b(43)[0]:ubyte) { return 0 }
  if (52 != f_b(17)[0]:ubyte) { return 0 }
  if (52 != f_b(98)[0]:ubyte) { return 0 }
  if (84 != f_b(120)[0]:ubyte) { return 0 }
  if (95 != f_b(25)[0]:ubyte) { return 0 }
  if (108 != f_b(127)[0]:ubyte) { return 0 }
  if (65 != f_b(26)[0]:ubyte) { return 0 }
  return 1;
}

function f_b(a:int):int {
  return 1024 + (23 + 37 * (a ^ 23130)) % 101
}


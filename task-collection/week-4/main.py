from math_operations import basic_operations, power_operation, apply_operations
# Test basic_operations
result_basic = basic_operations(10, 5)
print("Basic Operations Result:", result_basic)
# Test power_operation
result_power = power_operation(2, 3)
print("Power Operation Result:", result_power)
# Test power_operation with modulo

result_power_modulo = power_operation(2, 3, modulo=5)
print("Power Operation with Modulo Result:", result_power_modulo)

# Test apply_operations
operations = [

    (lambda x, y: x + y, (3, 4)),

    (lambda x, y: x * y, (2, 5)),

]


result_apply = apply_operations(operations)

print("Apply Operations Result:", result_apply)

Updated at: 2023-12-11 06:44:37.620686
Updated at: 2023-12-11 06:46:46.399902
Updated at: 2023-12-11 06:48:45.991648
Updated at: 2023-12-11 06:50:02.828088
Updated at: 2023-12-11 06:51:12.737255
Updated at: 2023-12-11 06:51:55.303242
Updated at: 2023-12-11 06:53:11.975735
Updated at: 2023-12-11 06:55:05.325527
Updated at: 2023-12-11 06:55:48.896910
Updated at: 2023-12-11 06:56:35.993243
Updated at: 2023-12-11 06:58:12.464091
Updated at: 2023-12-11 07:00:56.900543
Updated at: 2023-12-11 07:04:32.798777
Updated at: 2023-12-11 07:06:42.130334
Updated at: 2023-12-11 07:07:19.849528
Updated at: 2023-12-11 07:10:09.525906
Updated at: 2023-12-11 07:10:46.286029
Updated at: 2023-12-11 07:11:08.873033
Updated at: 2023-12-11 07:14:15.549285
Updated at: 2023-12-11 07:14:48.303468
Updated at: 2023-12-12 06:42:52.340322
Updated at: 2023-12-12 06:56:19.988921
Updated at: 2023-12-12 07:07:16.890963
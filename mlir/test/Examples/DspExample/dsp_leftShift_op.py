# RUN: toyc-ch2 %s -emit=mlir 2>&1 | FileCheck %s
def main() {
    var a = [2,3,4,5];
    var b = 1;
    var c = leftShift(a,b);
    print(c);
}
# CHECK-LABEL: toy.func @main()
# CHECK-NEXT:    [[VAL_0:%.*]] = toy.constant : tensor<*xi32>
# CHECK-NEXT:    [[VAL_1:%.*]] = toy.constant : tensor<*xi32>
# CHECK-NEXT:    [[VAL_2:%.*]] = toy.generic_call @leftShift([[VAL_0]], [[VAL_1]]) : (tensor<*xi32>, tensor<*xi32>) -> tensor<*xi32>
# CHECK-NEXT:    toy.print [[VAL_2]] : tensor<*xi32>
# CHECK-NEXT:    toy.return

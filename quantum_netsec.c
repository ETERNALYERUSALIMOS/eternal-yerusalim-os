#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>

MODULE_LICENSE("GPL");

static int __init quantum_init(void) {
    printk(KERN_INFO "IDEAL-OS Quantum v1.1 LOADED");
    return 0;
}

static void __exit quantum_exit(void) {
    printk(KERN_INFO "IDEAL-OS Quantum v1.1 UNLOADED");
}

module_init(quantum_init);
module_exit(quantum_exit);

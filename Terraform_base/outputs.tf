output "public_ip" {
  value = azurerm_public_ip.vm_pip.ip_address
}

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class FrmLogin : Form
    {
        public FrmLogin()
        {
            InitializeComponent();
            this.chkMostrarPass.Enabled = false;
        }

        private void FrmLogin_Load(object sender, EventArgs e)
        {
            this.lblHora.Text = DateTime.Now.ToString();

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //usar timer para mostrar la hora actual en la etiqueta hora
            this.lblHora.Text = DateTime.Now.ToString();
        }

        private void btnIngresar_Click(object sender, EventArgs e)
        {
            //hacer instancia de la clase login y verificar que todos las cajas esten llenas 
            Login obj = new Login();

            if (!obj.verificar(errorProvider1,txtUsuario,txtPass))
            {
                obj.MensajeErrror("Faltan algunos datos");
            }
        }

        private void chkMostrarPass_CheckedChanged(object sender, EventArgs e)
        {
            //mostrar contraseña oculta
                if (chkMostrarPass.Checked)
                {
                    this.txtPass.UseSystemPasswordChar = false;
                }
                else
                {
                    this.txtPass.UseSystemPasswordChar = true;
                }
    

        }

        private void txtPass_TextChanged(object sender, EventArgs e)
        {
            //si la caja de texto esta vacia, inabilitar el checkbox
            if (this.txtPass.Text=="")
            {
                chkMostrarPass.Enabled = false;
                chkMostrarPass.Checked = false;
            }
            else
            {
                chkMostrarPass.Enabled = true;
            }
        }

        private void lblNuevo_Click(object sender, EventArgs e)
        {
            //crear instancia del formulario nuevousuario 
            FrmNuevoUsuario obj = new FrmNuevoUsuario();
            obj.ShowDialog();

        }
    }
}

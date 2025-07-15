const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

console.log('Starting extraction of Crypto.zip...');

try {
  // Check if Crypto.zip exists
  if (!fs.existsSync('Crypto.zip')) {
    console.error('Crypto.zip not found in the current directory');
    process.exit(1);
  }

  // Create extraction directory
  const extractDir = 'extracted_crypto';
  if (!fs.existsSync(extractDir)) {
    fs.mkdirSync(extractDir, { recursive: true });
  }

  // Try to extract using unzip command (if available)
  try {
    execSync(`unzip -o Crypto.zip -d ${extractDir}`, { stdio: 'inherit' });
    console.log(`Successfully extracted Crypto.zip to ${extractDir}/`);
  } catch (error) {
    console.log('unzip command not available, trying alternative method...');
    
    // Alternative: Try using Node.js built-in modules
    // This is a fallback - we'll use a different approach
    console.log('Please manually extract Crypto.zip or use the following commands:');
    console.log('1. unzip Crypto.zip -d extracted_crypto');
    console.log('2. Or extract manually and copy files to the project directory');
  }

  // List contents of extraction directory
  if (fs.existsSync(extractDir)) {
    console.log('\nExtracted files:');
    const listFiles = (dir, prefix = '') => {
      const files = fs.readdirSync(dir);
      files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);
        if (stat.isDirectory()) {
          console.log(`${prefix}📁 ${file}/`);
          listFiles(filePath, prefix + '  ');
        } else {
          console.log(`${prefix}📄 ${file}`);
        }
      });
    };
    listFiles(extractDir);
  }

} catch (error) {
  console.error('Error during extraction:', error.message);
  console.log('\nAlternative methods to extract:');
  console.log('1. Use system unzip: unzip Crypto.zip');
  console.log('2. Use 7zip: 7z x Crypto.zip');
  console.log('3. Extract manually and copy files to project directory');
}